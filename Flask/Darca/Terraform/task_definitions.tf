resource "aws_ecs_task_definition" "ticket_submitter" {
  family = "ticket-submitter"
  container_definitions = <<DEFINITION
[
  {
    "name": "ticket-submitter",
    "image": "${docker_image.ticket_submitter.latest}",
    "portMappings": [
      {
        "containerPort": 5000,
        "hostPort": 5000
      }
    ],
    "essential": true
  }
]
DEFINITION
}

resource "aws_ecs_task_definition" "mongodb" {
  family = "mongodb"
  container_definitions = <<DEFINITION
[
  {
    "name": "mongodb",
    "image": "mongo:latest",
    "portMappings": [
      {
        "containerPort": 27017,
        "hostPort": 27017
      }
    ],
    "essential": true
  }
]
DEFINITION
}
