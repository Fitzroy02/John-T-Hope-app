# Consent Integration

## 1. Purpose

This guide explains how to implement parental consent mechanisms across the platform, ensuring transparency, respect, and compliance with age-tier requirements.

## 2. Scope

This guide applies to developers building consent workflows, instructors delivering sensitive content, and administrators managing parental permissions.

---

## 3. Consent Workflow Architecture

### 3.1 Consent Lifecycle

```
Module Created → Sensitivity Classification → Consent Requirement Determined 
    → Parent Notified → Consent Requested → Parent Responds 
    → Access Granted/Denied → Delivery Logged → Post-Access Summary
```

---

## 4. Sensitivity Classification

### 4.1 Sensitivity Levels

| **Level** | **Definition** | **Examples** | **Consent Required?** |
|-----------|----------------|--------------|----------------------|
| **Low** | General knowledge, no controversy | Maths, basic science, literacy | No |
| **Moderate** | Age-appropriate but potentially sensitive | Puberty, media literacy, historical events | Tier 1-2: Yes; Tier 3-4: Notification |
| **High** | Explicit, contested, or adult themes | Sexual health, geopolitics, identity topics | Tier 1-2: Yes; Tier 3: Yes; Tier 4: Opt-out |

### 4.2 Classification Process

**Automated Pre-Classification:**
- Keywords trigger sensitivity flags (e.g., "puberty," "sexuality," "politics")
- Content length and tier mismatch flagged for review

**Human Review:**
- Content creator assigns initial sensitivity level
- Reviewer confirms or adjusts classification
- Dual review required for high-sensitivity content

**Code Example (Pseudocode):**
```python
def classify_module_sensitivity(module):
    keywords = ["puberty", "sex", "politics", "religion", "identity"]
    if any(keyword in module.content.lower() for keyword in keywords):
        return "moderate"  # Requires human review
    return "low"
```

---

## 5. Parental Notification

### 5.1 Advance Notification Timeline

| **Tier** | **Sensitivity** | **Notification Window** |
|----------|-----------------|-------------------------|
| Tier 1-2 | Moderate/High | **2 weeks** before access |
| Tier 3 | High | **2 weeks** before access |
| Tier 4 | High | **2 weeks** before access (opt-out) |

### 5.2 Notification Content

Parents receive:
- **Module Title and Description**
- **Sensitivity Level and Tier Recommendation**
- **Learning Objectives**
- **Topics Covered** (detailed list)
- **Example Materials** (preview if available)
- **Consent Request or Opt-Out Instructions**

**Template (Tier 2 Example):**
```
Subject: Consent Required for Module Access: "Understanding Puberty"

Dear Parent/Guardian,

Your child will soon have the opportunity to access the module "Understanding Puberty" as part of their Tier 2 curriculum. This module covers:

- Physical changes during puberty
- Emotional and social development
- Hygiene and self-care
- Asking questions and seeking support

Sensitivity Level: Moderate
Age Tier: Tier 2 (Ages 9-12)

This module is designed to be age-appropriate, factual, and supportive. If you prefer to handle this education at home, you may opt out.

To provide consent: [Click Here]
To opt out: [Click Here]
To preview materials: [Click Here]

If you have questions, please contact us at education@platform.org.

Deadline to respond: [Date, 2 weeks from now]

If we do not hear from you by the deadline, we will assume you wish to opt out.

Thank you,
The Education Team
```

---

## 6. Consent Mechanisms

### 6.1 Opt-In (Tier 1-2, Moderate/High Sensitivity)

**Process:**
- Parent must actively click "I Consent" to grant access
- Silence or inaction = no access
- Parent can change decision at any time

**Code Example (Pseudocode):**
```python
def check_consent(learner, module):
    consent = database.query("consent_records", {
        "learner_id": learner.id,
        "module_id": module.id
    })
    if consent and consent.status == "granted":
        return True
    return False
```

---

### 6.2 Opt-Out (Tier 4, High Sensitivity)

**Process:**
- Parent is notified of upcoming content
- Learner can access unless parent actively opts out
- Silence or inaction = consent assumed

**Code Example (Pseudocode):**
```python
def check_consent_tier4(learner, module):
    opt_out = database.query("consent_records", {
        "learner_id": learner.id,
        "module_id": module.id,
        "status": "opted_out"
    })
    if opt_out:
        return False
    return True  # Consent assumed unless explicitly opted out
```

---

### 6.3 Acknowledgment (Tier 3, Moderate Sensitivity)

**Process:**
- Parent receives notification but does not need to grant explicit consent
- Parent can request more information or opt out if concerned
- Learner can access by default

---

## 7. Alternative Provision

### 7.1 When a Parent Opts Out

**What the Learner Receives Instead:**
- A take-home resource pack for parent-led learning
- Links to external, parent-approved materials
- An alternative assignment (if applicable)

**What the Learner Does Not Receive:**
- Access to the module
- Penalisation or disadvantage in assessments

---

## 8. Consent Data Management

### 8.1 Consent Record Schema

```json
{
  "id": "consent_12345",
  "learner_id": "learner_67890",
  "module_id": "module_abc",
  "parent_id": "parent_11111",
  "status": "granted",  // "granted", "denied", "opted_out", "pending"
  "timestamp": "2026-02-01T10:00:00Z",
  "expiry": "2027-02-01T10:00:00Z",  // Consent expires after 1 year
  "notes": "Parent requested preview materials before consenting"
}
```

### 8.2 Consent Expiry

Consent is time-limited:
- **Tier 1-2:** Consent valid for **1 year**
- **Tier 3-4:** Consent valid for **2 years**

Parents are re-notified and asked to reconfirm consent before expiry.

---

## 9. Revoking Consent

### 9.1 Parent-Initiated Revocation

Parents may revoke consent at any time:
- Learner's access is immediately disabled
- Parent receives confirmation of revocation
- Learner is notified (age-appropriately)

**Code Example (Pseudocode):**
```python
def revoke_consent(learner_id, module_id):
    database.update("consent_records", {
        "learner_id": learner_id,
        "module_id": module_id
    }, {
        "status": "revoked",
        "revoked_at": current_timestamp()
    })
    disable_module_access(learner_id, module_id)
    notify_parent("Consent revoked successfully.")
```

---

## 10. Post-Access Summary

### 10.1 What Parents See After Module Completion

Parents receive:
- Confirmation that their child completed the module
- Summary of topics covered
- Any questions the learner asked during the module
- Invitation to discuss with their child

**Template:**
```
Subject: Module Completed: "Understanding Puberty"

Dear Parent/Guardian,

Your child has successfully completed the module "Understanding Puberty."

Topics covered:
- Physical changes during puberty
- Hygiene and self-care
- Emotional development

Your child asked the following question during the module:
- "When do growth spurts usually happen?"

We encourage you to discuss this topic with your child at home.

If you have concerns or feedback, please contact us at education@platform.org.

Thank you,
The Education Team
```

---

## 11. Consent Metrics and Reporting

### 11.1 Platform-Wide Consent Metrics

Track and report:
- Percentage of parents granting consent (by tier and module)
- Opt-out rates for Tier 4 content
- Average response time for consent requests
- Revocation rates

### 11.2 Use of Metrics

Metrics inform:
- Module sensitivity classification accuracy
- Parent communication effectiveness
- Need for alternative materials

---

## 12. Review and Continuous Improvement

Consent workflows are reviewed:
- Quarterly for efficiency and clarity
- Annually for compliance with legislation
- Following parent feedback or complaints

---

**Consent is not a checkbox. It is a relationship.**
