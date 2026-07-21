# Workshop Restructure Summary

## Overview

The workshop has been streamlined to focus on **Flink + Tableflow + Open Standards**, with Data Governance (CSFLE and Data Quality Rules) integrated into LAB 1 and Snowflake available as a collapsible alternative to Athena throughout LAB 1 and LAB 2.

---

## What Changed

### Lab 1: Payment Validation and Tableflow Deep Dive
**Duration:** ~40-50 minutes

#### Structure
- **Part 1: Data Governance** (NEW - comes first)
  - Client-Side Field Level Encryption (CSFLE) - encrypt sensitive credit card data
  - Data Quality Rules - validate confirmation codes with DLQ routing
  - Single ECS restart picks up both rules
  - Verify both encryption and DQR are working
- **Part 2: Payment Processing with Flink** (unchanged core content)
  - Get Started with Flink SQL
  - Payment Deduplication
  - Creating Completed Orders with Interval Joins
- **Part 3: Setting up Tableflow** (unchanged)
- **Part 4: Tableflow Deepdive** (expanded with Snowflake)
  - Optional Snowflake one-time setup (collapsible)
  - All query sections offer both Athena and Snowflake options (collapsible)
  - Schema Evolution, Time Travel, Partitioning, Monitoring

#### Key Changes
- ✅ **CSFLE integrated** from former BONUS lab into Part 1
- ✅ **Data Quality Rules** moved from Part 3 to Part 1 (before Flink)
- ✅ **Snowflake** available as collapsible alternative throughout Part 4
- ✅ All query sections use `<details>` collapsibles for engine choice

---

### Lab 2: Product Sales and Customer360 Aggregation
**Duration:** ~30-40 minutes (optional)

#### Key Changes
- ✅ **Snowflake Iceberg table creation** added as collapsible after Tableflow enablement
- ✅ **Query section** converted to collapsible Athena + Snowflake pair
- ✅ Navigation links updated (BONUS reference removed)

#### What Remains (Unchanged)
- Building enriched customer data product
- Product sales data product with temporal joins
- Customer 360 snapshot with window functions
- Tableflow setup and enablement

---

### BONUS Lab: Data Contracts and Encryption
- **Deprecated** - content integrated into LAB 1 Part 1
- File retained with deprecation notice for reference
- CSFLE and DQR content now part of the main lab flow

---

### Snowflake Integration
- **No longer a separate lab** - integrated as collapsible alternative throughout LAB 1 and LAB 2
- Users choose between Athena and Snowflake at each query section
- One-time Snowflake setup (catalog integration + external volume + IAM trust policies) is a collapsible section in LAB 1 Part 4
- Snowflake SQL syntax differences handled (e.g., `DATEADD` instead of `+ INTERVAL`)
- Snowflake limitations documented (no `$snapshots`/`$partitions` metadata tables for external Iceberg)

---

## Time Breakdown

### Current Workshop (~60-75 minutes)
- **Lab 1:** ~40-50 min (Data Governance + Flink + Tableflow Deep Dive)
- **Lab 2:** ~30-40 min (Optional - Product Sales + Customer360)

**Tableflow Coverage:** Deep dive with schema evolution, time travel, partitioning, monitoring
**Engine Coverage:** Athena + Snowflake (user's choice)

---

## Key Benefits

### For Attendees
1. **Data Governance First**: CSFLE and DQR set up before data processing, reflecting real-world best practices
2. **Engine Flexibility**: Choose between Athena and Snowflake for all query exercises
3. **Deeper Learning**: More hands-on time with Tableflow capabilities
4. **Clearer Narrative**: Focused story arc (Governance → Flink → Tableflow → Multi-Engine)

### For Instructors
1. **Less Troubleshooting**: Fewer separate labs to manage
2. **Stronger Demo**: Data governance + multi-engine queries are impressive
3. **Easier Timing**: Collapsible sections let attendees self-pace
4. **Better Positioning**: Emphasizes Confluent differentiation (Governance + Tableflow)

---

## What Attendees Learn

### Lab 1
- **Data Governance**: CSFLE encryption, PII tagging, data quality rules, DLQ routing
- **Flink SQL**: Stream joins (regular and interval), deduplication, watermarks
- **Tableflow**: Iceberg materialization, schema evolution, time travel, partitioning, monitoring
- **Multi-Engine Querying**: Athena and/or Snowflake on same Iceberg tables

### Lab 2 (Optional)
- **Advanced Flink**: Temporal joins, window functions, CDC handling
- **Data Products**: Enriched customers, product sales, customer 360 snapshot
- **Tableflow**: Multi-table enablement, cross-table analytics

---

## Notes for Workshop Delivery

### Pre-Lab Setup Checklist
- [ ] Verify S3 bucket created (required for Tableflow BYOS)
- [ ] Confirm Glue Data Catalog is accessible
- [ ] Test Athena query editor access
- [ ] If demonstrating Snowflake: verify ACCOUNTADMIN access

### Common Gotchas
1. **Tableflow Lag**: Remind attendees data takes 5-15 min to appear for querying
2. **Cluster ID**: Provide clear instructions on finding cluster ID for Athena/Snowflake
3. **Schema Evolution**: Emphasize stopping old Flink statement before recreating table
4. **Snowflake IAM**: Both catalog and storage trust entries needed on same role
5. **CSFLE**: Only messages after ECS restart will be encrypted

### Recommended Break Points
- After Part 1 Data Governance completion
- During Tableflow materialization wait time in Part 3

---

## Feedback Questions for Attendees

At the end of the workshop, ask:

1. Did the data governance section (CSFLE + DQR) add value to your learning?
2. Which query engine did you use (Athena, Snowflake, or both)?
3. Was the schema evolution demonstration valuable?
4. Which Tableflow feature was most impressive? (time travel, auto-partitioning, etc.)
5. How likely are you to use Tableflow in your architecture?
