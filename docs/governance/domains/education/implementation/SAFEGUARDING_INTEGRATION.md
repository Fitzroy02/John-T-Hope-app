# Safeguarding Integration

## 1. Purpose

This guide explains how safeguarding is embedded into every aspect of educational delivery on the platform.

## 2. Scope

This guide applies to all platform developers, instructors, content creators, and administrators involved in educational services.

---

## 3. Safeguarding Principles

### 3.1 Visibility
All interactions between instructors and learners are visible, logged, and auditable.

### 3.2 Accountability
Instructors and content creators are accountable for maintaining safeguarding standards.

### 3.3 Proactive Protection
The platform uses automated monitoring and human oversight to detect and prevent harm before it occurs.

### 3.4 Escalation
Safeguarding concerns are escalated immediately to trained officers with authority to act.

---

## 4. Technical Safeguarding Features

### 4.1 Interaction Logging

**What is Logged:**
- All messages between instructors and learners
- Video call recordings and transcripts
- Content shared or viewed
- Timestamps and session durations

**How it Works:**
- Logs are stored in a secure, encrypted database
- Logs are accessible to safeguarding officers and parents
- Logs are retained for 7 years

**Code Example (Pseudocode):**
```python
def log_interaction(learner_id, instructor_id, interaction_type, content):
    interaction = {
        "id": generate_unique_id(),
        "learner_id": learner_id,
        "instructor_id": instructor_id,
        "timestamp": current_timestamp(),
        "interaction_type": interaction_type,
        "content": content,
        "flagged": False
    }
    database.insert("interaction_logs", interaction)
    check_for_safeguarding_triggers(interaction)
```

---

### 4.2 Real-Time Monitoring

**Automated Triggers:**
- Keyword detection (e.g., "secret," "don't tell," "meet me")
- Unusual interaction patterns (e.g., excessive one-to-one contact, late-night messaging)
- Rapid escalation of intimacy or personal disclosure

**Response:**
- Alert sent to safeguarding officer immediately
- Interaction flagged for human review
- Instructor notified of concern (if appropriate)

**Code Example (Pseudocode):**
```python
SAFEGUARDING_KEYWORDS = ["secret", "don't tell", "meet me", "alone"]

def check_for_safeguarding_triggers(interaction):
    for keyword in SAFEGUARDING_KEYWORDS:
        if keyword in interaction["content"].lower():
            flag_interaction(interaction)
            alert_safeguarding_officer(interaction)
```

---

### 4.3 Age-Tier Access Control

**Enforcement:**
- Learners can only access content approved for their tier
- System prevents instructors from delivering higher-tier content without consent override

**Code Example (Pseudocode):**
```python
def can_access_module(learner, module):
    if learner.age_tier < module.age_tier:
        if not has_parental_consent(learner, module):
            return False
    return True
```

---

### 4.4 No Direct Messaging

**Enforcement:**
- Platform does not support private, unmonitored messaging between instructors and learners
- All communication occurs in logged, visible environments

**Implementation:**
- Disable DM features for instructor-learner pairs
- Route all communication through Q&A forums or classroom chat (logged)

---

## 5. Human Safeguarding Oversight

### 5.1 Safeguarding Officer Role

**Responsibilities:**
- Monitor automated alerts
- Investigate flagged interactions
- Interview learners, instructors, and parents as needed
- Escalate to law enforcement if necessary

**Qualifications:**
- Safeguarding training (e.g., UK Safer Recruitment, DBS checks)
- Child protection certification
- Experience in educational or youth work settings

---

### 5.2 Quarterly Audits

**Process:**
- Random sample of 10% of instructors reviewed each quarter
- Audit includes:
  - Interaction logs
  - Content delivered
  - Feedback from learners and parents
  - Compliance with tier restrictions

**Outcome:**
- Instructors cleared, retrained, or removed based on findings

---

### 5.3 Incident Response

**If a safeguarding concern is raised:**

1. **Immediate Action** (within 1 hour):
   - Suspend instructor access if risk is high
   - Secure all logs and evidence
   - Notify parents if learner is involved

2. **Investigation** (within 48 hours):
   - Review all relevant interactions
   - Interview involved parties
   - Determine severity and appropriate response

3. **Resolution** (within 7 days):
   - Reinstate, retrain, or remove instructor
   - Provide report to parents and platform leadership
   - Update safeguarding protocols if gaps are identified

---

## 6. Parental Safeguarding Tools

### 6.1 Interaction Log Access

Parents can:
- View all interactions between their child and instructors
- Request full transcripts of video sessions
- Filter logs by date, instructor, or module

**Implementation:**
```python
def get_learner_interactions(learner_id, parent_id):
    if not is_parent_of(parent_id, learner_id):
        return "Access Denied"
    return database.query("interaction_logs", {"learner_id": learner_id})
```

---

### 6.2 Emergency Reporting

Parents can:
- Flag interactions for immediate review
- Request instructor removal from their child's learning
- Report concerns anonymously

**Response Time:**
- Emergency reports reviewed within **1 hour**
- High-priority reports reviewed within **24 hours**

---

## 7. Instructor Safeguarding Training

### 7.1 Mandatory Training Modules

All instructors must complete:
- **Safeguarding Basics** (2 hours): Recognising abuse, reporting procedures
- **Professional Boundaries** (1 hour): Appropriate conduct, avoiding favouritism
- **Platform Tools** (1 hour): Using interaction logs, escalation procedures

### 7.2 Annual Refreshers

Instructors complete annual refresher training to stay updated on:
- New safeguarding legislation
- Platform policy changes
- Emerging risks (e.g., AI deepfakes, online grooming tactics)

---

## 8. Safeguarding Metrics and Reporting

### 8.1 Platform-Wide Metrics

Track and report:
- Number of flagged interactions per month
- Response times to safeguarding alerts
- Instructor suspensions and removals
- Parental complaints and resolutions

### 8.2 Transparency

Publish annual safeguarding report including:
- Total incidents investigated
- Outcomes (unfounded, training required, removal)
- Improvements made to safeguarding systems

---

## 9. Review and Continuous Improvement

Safeguarding integration is reviewed:
- Quarterly by safeguarding officers
- Annually by external auditors
- Following any serious incident

---

**Safeguarding is not a feature. It is the foundation.**
