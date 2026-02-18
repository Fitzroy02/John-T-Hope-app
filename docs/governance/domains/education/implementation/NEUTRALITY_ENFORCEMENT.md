# Neutrality Enforcement

## 1. Purpose

This guide explains how to enforce neutrality in educational content through review processes, instructor training, and feedback mechanisms.

## 2. Scope

This guide applies to content reviewers, instructors, curriculum designers, and platform administrators responsible for maintaining educational neutrality.

---

## 3. Neutrality Enforcement Framework

### 3.1 Three-Stage Process

```
Content Creation → Neutrality Review → Safeguarding Review → Approval → Delivery → Ongoing Monitoring
```

---

## 4. Neutrality Review Process

### 4.1 When Neutrality Review is Required

**Automatic Triggers:**
- Content classified as "moderate" or "high" sensitivity
- Content covering topics listed in sensitive subjects (politics, religion, identity, sexuality, geopolitics)
- Parent or learner flags content for review

### 4.2 Reviewer Qualifications

**Neutrality Reviewers Must:**
- Have subject matter expertise
- Be trained in recognising bias and ideological framing
- Represent diverse perspectives (political, cultural, religious)
- Declare conflicts of interest

---

## 5. Neutrality Review Checklist

### 5.1 Language and Framing

**Questions to Ask:**
- [ ] Does the content use neutral, descriptive language?
- [ ] Are value-laden terms (e.g., "oppression," "progress," "natural") used critically or uncritically?
- [ ] Is the framing balanced, or does it privilege one perspective?

**Red Flags:**
- Phrases like "everyone agrees," "it is obvious," "the right side of history"
- Moral judgments presented as facts
- Emotive language designed to persuade rather than inform

**Example:**
- ❌ **Not Neutral:** "Capitalism exploits workers and creates inequality."
- ✅ **Neutral:** "Capitalism is criticised for creating inequality by some scholars, while others argue it promotes innovation and prosperity."

---

### 5.2 Perspective Balance

**Questions to Ask:**
- [ ] Are multiple perspectives represented?
- [ ] Are dissenting or minority views included?
- [ ] Is one perspective presented as "enlightened" or "correct"?

**Red Flags:**
- Only one side of a contested debate is presented
- Opposing views are strawmanned or dismissed
- Perspectives aligned with Western, secular, progressive values are privileged

**Example:**
- ❌ **Not Neutral:** "Same-sex marriage is a human right."
- ✅ **Neutral:** "Same-sex marriage is supported by those who argue it is a matter of equality. Others oppose it based on religious or cultural beliefs. Laws vary globally."

---

### 5.3 Source Quality and Diversity

**Questions to Ask:**
- [ ] Are sources credible and peer-reviewed?
- [ ] Are sources ideologically diverse?
- [ ] Are funding sources or conflicts of interest disclosed?

**Red Flags:**
- Reliance on advocacy organisations (e.g., Greenpeace, Heritage Foundation) without labelling them as such
- Use of opinion pieces or blogs as authoritative sources
- Exclusion of credible counter-evidence

---

### 5.4 Contextualisation of Controversy

**Questions to Ask:**
- [ ] Is it acknowledged where disagreement or uncertainty exists?
- [ ] Are contested topics framed as open questions rather than settled truths?
- [ ] Is the historical or cultural context provided?

**Red Flags:**
- Presenting emerging theories as settled science
- Ignoring cultural or religious diversity on moral issues
- Treating contemporary controversies as historical facts

**Example:**
- ❌ **Not Neutral:** "Climate change is caused by human activity, and we must act now."
- ✅ **Neutral:** "The majority of climate scientists agree that human activity contributes to climate change. There is debate about the extent and the best responses."

---

## 6. Neutrality Review Outcomes

### 6.1 Approved
Content is cleared for delivery without changes.

### 6.2 Revisions Required
Reviewer provides specific feedback on language, framing, or sources.  
Content creator revises and resubmits.

### 6.3 Rejected
Content is ideologically biased, factually inaccurate, or inappropriate for the tier.  
Content creator must redesign or withdraw.

---

## 7. Dual Review for High-Sensitivity Content

### 7.1 Why Dual Review?

High-sensitivity topics (recent history, identity, religion, sexuality, geopolitics) are reviewed by:
- **Neutrality Reviewer**: Ensures balanced framing
- **Safeguarding Reviewer**: Ensures age-appropriateness and learner safety

Both must approve before content is delivered.

### 7.2 Disagreement Resolution

If reviewers disagree:
- A third senior reviewer is consulted
- Platform governance lead makes the final decision
- Decision rationale is documented

---

## 8. Instructor Training on Neutrality

### 8.1 Mandatory Training Modules

**Module 1: Recognising Bias (2 hours)**
- What is bias vs. perspective?
- Common forms of ideological framing
- Case studies of non-neutral content

**Module 2: Teaching Contested Topics (2 hours)**
- How to present multiple perspectives
- Handling learner questions on sensitive issues
- Avoiding moral judgments

**Module 3: Neutrality in Practice (1 hour)**
- Using the neutrality review checklist
- Escalating concerns about content
- Role-playing scenarios

### 8.2 Annual Refresher
Instructors complete a 1-hour refresher annually covering:
- Updates to sensitive subject lists
- Common neutrality mistakes identified in audits
- New case studies

---

## 9. Learner and Parent Feedback

### 9.1 Flagging Content for Review

Parents and learners can flag content if they believe it:
- Advocates for a political ideology
- Presents contested issues as settled truth
- Excludes important perspectives
- Moralises on sensitive topics

### 9.2 Flagging Process

**Step 1: Submit Flag**
Parent/learner submits a flag via platform, including:
- Module or lesson title
- Specific content of concern
- Reason for concern

**Step 2: Acknowledgment**
Platform acknowledges receipt within **24 hours**.

**Step 3: Review**
Neutrality reviewer assesses flagged content within **7 days**.

**Step 4: Response**
Parent/learner receives:
- Summary of review findings
- Action taken (content revised, approved, or removed)
- Rationale for decision

**Code Example (Pseudocode):**
```python
def flag_content(module_id, user_id, reason):
    flag = {
        "id": generate_unique_id(),
        "module_id": module_id,
        "user_id": user_id,
        "reason": reason,
        "timestamp": current_timestamp(),
        "status": "pending_review"
    }
    database.insert("content_flags", flag)
    notify_reviewers(flag)
```

---

## 10. Ongoing Monitoring

### 10.1 Post-Delivery Monitoring

Even after approval, content is monitored for:
- Patterns of parent/learner complaints
- Changes in cultural or political context
- New evidence or scholarship

### 10.2 Quarterly Audits

**Process:**
- Random sample of 10% of modules reviewed each quarter
- Focus on high-sensitivity topics
- Findings inform training and policy updates

---

## 11. Neutrality Metrics and Reporting

### 11.1 Platform-Wide Neutrality Metrics

Track and report:
- Number of modules flagged for neutrality concerns
- Approval vs. revision vs. rejection rates
- Time to review and resolve flags
- Common neutrality mistakes by content creators

### 11.2 Transparency

Publish annual neutrality report including:
- Total reviews conducted
- Common issues identified
- Improvements made to review processes

---

## 12. Review and Continuous Improvement

Neutrality enforcement is reviewed:
- Quarterly by content governance team
- Annually by external auditors
- Following significant cultural or political events

---

**Neutrality is not neutralising. It is equipping learners to think critically.**
