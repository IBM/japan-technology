# Project Documentation Rules (Non-Obvious Only)

## Workshop Structure
- **Three separate paths**: LAB1, LAB2, and Shiftleft are INDEPENDENT - LAB1/LAB2 are step-by-step workshops, Shiftleft is continuous end-to-end demo
- **LAB1 is prerequisite**: LAB2 builds on LAB1 concepts but Shiftleft is standalone
- **Time estimates matter**: LAB1 is 40-50 min, LAB2 is 30-40 min optional - workshop designed for 90 min total including 30 min setup

## Infrastructure Deployment
- **Setup takes 7-10 minutes**: Terraform provisioning is NOT instant - users need to wait for RDS, ECS, and Confluent Cloud resources
- **Same shell requirement**: AWS credentials MUST be in same terminal as terraform commands - this is a common gotcha
- **Destroy script required**: Direct `terraform destroy` will fail - must use `demo-destroy.sh` which handles Tableflow/catalog cleanup first

## Data Flow Timing
- **Tableflow lag is expected**: 5-15 minutes for data to appear in Glue/Athena/Snowflake after enabling - this is NOT a bug
- **ECS restart timing**: After schema changes, wait 1-2 minutes for new ECS task to start before checking results
- **CDC connector may fail first time**: PostgreSQL not ready on initial deploy - this is documented and expected

## Flink SQL Behavior
- **"Running" status is normal**: Flink statements run continuously - they don't "complete" like batch queries
- **Backticks required**: CDC tables need full path with backticks: `` `prefix.schema.table_name` ``
- **Stop before schema evolution**: Must stop Flink statement before recreating table with new schema

## Snowflake vs Athena
- **Two separate IAM trust entries**: Snowflake needs BOTH Glue catalog integration AND external volume trust policies on SAME role
- **Snowflake is optional**: All labs work with Athena - Snowflake sections are collapsible alternatives
- **No metadata tables in Snowflake**: External Iceberg tables don't support `$snapshots` or `$partitions` queries

## Common Misconceptions
- **Not a production template**: This is educational infrastructure - designed for deploy/learn/destroy cycle
- **Pre-built images**: Participants do NOT build Docker images - they're pre-built on ECR Public
- **No automated tests**: Validation is manual via Confluent Cloud UI and AWS Console