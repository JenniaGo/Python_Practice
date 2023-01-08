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
