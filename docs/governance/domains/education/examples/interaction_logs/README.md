# Interaction Logs Examples

## Purpose

This directory contains example interaction logs demonstrating how instructor-learner interactions are recorded, monitored, and reviewed for safeguarding compliance.

## Contents

Example logs will be added here that demonstrate:
- Proper use of the `interaction_log.schema.json`
- Different interaction types (question, response, feedback, flagged_event)
- Safeguarding flagging and review processes
- Visibility and retention policies
- Parent notification workflows

## Example Structure

### Standard Interaction

```json
{
  "id": "log_20260218_001",
  "learner_id": "learner_12345",
  "instructor_id": "instructor_67890",
  "module_id": "module_math_101",
  "timestamp": "2026-02-18T10:30:00Z",
  "interaction_type": "question",
  "content": "Can you explain how to solve quadratic equations?",
  "flagged": false,
  "visibility": "parent",
  "retention_until": "2033-02-18"
}
```

### Flagged Interaction

```json
{
  "id": "log_20260218_002",
  "learner_id": "learner_12345",
  "instructor_id": "instructor_67890",
  "module_id": "module_puberty_education_t2",
  "timestamp": "2026-02-18T11:00:00Z",
  "interaction_type": "flagged_event",
  "content": "Instructor mentioned meeting after class",
  "flagged": true,
  "flagged_reason": "Safeguarding keyword detected: 'meet me'",
  "flagged_by": "system",
  "reviewed": true,
  "reviewed_by": "safeguarding_officer_01",
  "reviewed_date": "2026-02-18T12:00:00Z",
  "review_outcome": "no_action_required",
  "parent_notified": false,
  "visibility": "admin_only",
  "retention_until": "2033-02-18",
  "notes": "Context reviewed: Instructor was clarifying optional office hours for questions."
}
```

## How to Use

Developers should:
1. Implement interaction logging for all instructor-learner communications
2. Use automated flagging for safeguarding keywords and patterns
3. Ensure logs are accessible to parents and administrators
4. Follow retention policies (7 years minimum)
5. Protect learner privacy while maintaining transparency

---

**These logs are the foundation of safeguarding accountability.**
