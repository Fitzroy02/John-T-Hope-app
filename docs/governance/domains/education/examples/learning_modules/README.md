# Learning Modules Examples

## Purpose

This directory contains example learning modules demonstrating how to structure educational content according to the age-tiered curriculum design principles.

## Contents

Example modules will be added here that demonstrate:
- Proper use of the `learning_module.schema.json`
- Age-appropriate content for each tier (1-4)
- Sensitivity classification and consent requirements
- Safeguarding and neutrality review documentation
- Transparent authorship and version control

## Example Structure

Each example module should include:

```json
{
  "id": "module_example_tier2_puberty",
  "title": "Understanding Puberty",
  "age_tier": 2,
  "subject_area": "Health Education",
  "sensitivity_level": "moderate",
  "requires_parental_consent": true,
  "safeguarding_reviewed": {
    "reviewed": true,
    "reviewed_by": "safeguarding_officer_01",
    "reviewed_date": "2026-01-15",
    "approved": true,
    "notes": "Age-appropriate language confirmed"
  },
  "neutrality_reviewed": {
    "reviewed": true,
    "reviewed_by": "neutrality_reviewer_02",
    "reviewed_date": "2026-01-15",
    "approved": true,
    "notes": "Content is descriptive and non-judgmental"
  },
  "authorship": {
    "primary_author": "Dr. Sarah Johnson",
    "contributors": ["Health Education Team"],
    "creation_date": "2026-01-10",
    "organisation": "Platform Education Services",
    "conflicts_of_interest": "None"
  },
  "version": "1.0.0",
  "notes": "This module requires explicit parental consent before learner access."
}
```

## How to Use

Content creators should:
1. Review existing examples before creating new modules
2. Validate new modules against the schema
3. Follow the age-tier design principles
4. Ensure all required reviews are completed
5. Document authorship transparently

---

**These examples demonstrate best practices in educational governance.**
