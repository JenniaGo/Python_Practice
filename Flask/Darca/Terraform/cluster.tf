resource "aws_ecs_service" "mongodb" {
  name = "mongodb-service"
  cluster = aws_ecs_cluster.ticket_submitter.id
  task_definition = aws_ecs_task_definition.mongodb.arn
  desired_count = 1
}

resource "aws_ecs_service" "ticket_submitter" {
  depends_on = [aws_ecs_service.mongodb]
  name = "ticket-submitter-service"
  cluster = aws_ecs_cluster.ticket_submitter.id
  task_definition = aws_ecs_task_definition.ticket_submitter.arn
  desired_count = 1
}

resource "aws_alb_listener" "http" {
  load_balancer_arn = aws_alb.ticket_submitter.arn
  port = "80"
  protocol = "HTTP"

  default_action {
    type = "forward"
    target_group_arn = aws_alb_target_group.ticket_submitter.arn
  }
}

resource "aws_alb" "ticket_submitter" {
  name = "ticket-submitter-alb"
  internal = true
  security_groups = [aws_security_group.ticket_submitter.id]
  subnets = aws_subnet.ticket_submitter[*].id
  idle_timeout = 60
}

resource "aws_alb_target_group" "ticket_submitter" {
  name = "ticket-submitter-tg"
  port = 5000
  protocol = "HTTP"
  vpc_id = aws_vpc.ticket_submitter.id
  target_type = "ip"
}

resource "aws_security_group" "ticket_submitter" {
  name = "ticket-submitter-sg"
  vpc_id = aws_vpc.ticket_submitter.id

  ingress {
    from_port = 5000
    to_port = 5000
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

 
