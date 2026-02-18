# Parent & Guardian Consent Flow

**Clear, informed consent procedures for families engaging with the John T Hope Centre.**

---

## Purpose

The consent flow ensures that:

- Parents and guardians provide **informed, voluntary consent**
- Consent is **age-appropriate and revocable**
- The Centre operates with **transparency and accountability**
- Safeguarding protections are **consistently maintained**
- All consent is **logged with authorship and timestamps**

This is not a commercial transaction.  
This is a **civic agreement** built on trust, transparency, and mutual responsibility.

---

## Consent Principles

All consent processes at the John T Hope Centre are guided by:

### 1. Informed Consent
- Clear explanation of what is being consented to
- Plain language, accessible to all reading levels
- Transparency about data use, content access, and institutional purpose
- No hidden implications or unstated consequences

### 2. Voluntary Consent
- No coercion or pressure to consent
- Clear alternatives if consent is declined
- Respect for autonomous decision-making
- No penalties for non-consent

### 3. Revocable Consent
- Consent can be withdrawn at any time
- No justification required for withdrawal
- Simple, clear withdrawal process
- Prompt institutional response to withdrawal

### 4. Age-Appropriate Consent
- Consent tailored to developmental stage
- Age-tier alignment
- Protection of younger learners through parental authority
- Gradual autonomy as learners mature

### 5. Transparent Consent
- Clear documentation of consent status
- Accessible consent records for families
- Ongoing review and renewal mechanisms
- No hidden changes to consent terms

### 6. Logged Consent
- All consent recorded with timestamps
- Clear authorship of consent decisions
- Auditable consent trail
- Accountability for institutional actions

---

## Six-Step Consent Flow

### Step 1: Identity Verification

**Purpose:** Establish that the person providing consent is a legal parent or guardian.

**Process:**
- Parent or guardian creates account
- Identity verification through institutional process
- Relationship to learner confirmed
- Account linked to learner profile

**Safeguarding Note:** Identity verification protects against unauthorized access and ensures parental authority is respected.

---

### Step 2: Age-Tier Assignment

**Purpose:** Assign learner to appropriate age-tier for content access.

**Process:**
- Learner's date of birth confirmed
- Age-tier automatically assigned based on age
- Tier-specific content boundaries explained
- Parent/guardian informed of tier implications

**Tiers:**
- **Tier 1:** Ages 5-7 (early childhood)
- **Tier 2:** Ages 8-10 (middle childhood)
- **Tier 3:** Ages 11-13 (early adolescence)
- **Tier 4:** Ages 14-16 (mid-adolescence)
- **Tier 5:** Ages 17-18 (late adolescence)
- **Tier 6:** Ages 18+ (adult learners)

**Safeguarding Note:** Age-tier assignment ensures content is developmentally appropriate and protects younger learners from exposure to inappropriate material.

---

### Step 3: Consent Options Presented

**Purpose:** Give parents/guardians clear, specific consent choices.

**Four Consent Categories:**

#### 3.1 General Access Consent
- Access to age-tier-appropriate general curriculum
- Access to public learning materials
- Participation in asynchronous learning activities
- **Default:** Not granted until explicitly consented

#### 3.2 Sensitive Content Consent
- Access to age-appropriate sensitive topics (e.g., historical violence, ethical dilemmas, complex social issues)
- Advanced materials within age tier
- Content requiring higher maturity within tier
- **Default:** Not granted until explicitly consented

#### 3.3 Data Processing Consent
- Processing of learner progress data
- Aggregated, anonymized analytics
- Institutional use for curriculum improvement
- **Default:** Not granted until explicitly consented
- **Note:** Minimal data only; no commercial use

#### 3.4 Live Interaction Consent
- Participation in live sessions (if/when offered)
- Interaction with instructors or other learners
- Real-time engagement activities
- **Default:** Not granted until explicitly consented

**Presentation:**
- Each consent option explained in plain language
- Implications clearly stated
- Parent/guardian can consent to any combination
- Consent can be partially granted (e.g., general access without sensitive content)

**Safeguarding Note:** Granular consent allows parents to tailor engagement to family values and learner maturity.

---

### Step 4: Consent Logging

**Purpose:** Create auditable, transparent record of consent decisions.

**Process:**
- Each consent decision logged to database
- Record includes:
  - Consent type (general_access, sensitive_content, data_processing, live_interaction)
  - Granted status (true/false)
  - Timestamp of consent
  - Expiration date (if applicable)
  - Parent/guardian ID (authorship)
  - Learner ID
  - Optional notes field for context

**Schema Reference:** See `consent_status.schema.json` in `docs/governance/schemas/`

**Safeguarding Note:** Logging ensures accountability and provides audit trail for institutional decisions.

---

### Step 5: Ongoing Review

**Purpose:** Ensure consent remains current and reflective of family preferences.

**Process:**
- Annual consent review reminder sent to parents/guardians
- Automatic notification when learner transitions to new age tier
- Easy access to consent dashboard
- Simple process to update or revoke consent

**Triggers for Review:**
- Annual anniversary of initial consent
- Age-tier transition
- Institutional changes to consent categories
- Parent/guardian request

**Safeguarding Note:** Ongoing review respects evolving family circumstances and learner development.

---

### Step 6: Safeguarding Integration

**Purpose:** Ensure consent decisions align with safeguarding standards.

**Process:**
- All consent decisions reviewed against safeguarding policy
- Automatic flags if consent patterns suggest risk (e.g., adult requesting access to child-tier content)
- Safeguarding Board notified of concerning patterns
- Manual review for edge cases

**Safeguarding Board Authority:**
- Can override consent decisions if safeguarding concern exists
- Must document reasoning for override
- Must notify parent/guardian of decision
- Subject to appeal and review

**Safeguarding Note:** Safeguarding always takes precedence over consent preferences.

---

## Consent Withdrawal

### How to Withdraw Consent

Parents/guardians can withdraw consent at any time through:

1. **Consent Dashboard**
   - Online portal
   - Toggle consent categories off
   - Changes take effect immediately

2. **Written Request**
   - Email or written communication
   - Processed within 48 hours
   - Confirmation sent to parent/guardian

3. **Complete Disengagement**
   - Request to close learner account
   - All data deleted within 30 days (or legal retention minimum)
   - Confirmation of deletion sent to parent/guardian

### What Happens After Withdrawal

- Access to relevant content/activities immediately revoked
- Data processing stops (except legal retention requirements)
- No penalties or pressure to re-consent
- Re-engagement possible at any time through new consent process

---

## Consent for Adult Learners

Learners aged 18+ provide their own consent.

**Process:**
- Adult learner creates own account
- Identity verification required
- Self-consent to all categories
- Same revocability and transparency principles apply

**Note:** Adult learners have full autonomy over consent decisions.

---

## Special Circumstances

### Court-Ordered Access Restrictions
If a learner is subject to court-ordered access restrictions, the Centre:
- Requires documentation of restrictions
- Implements restrictions in system
- Notifies relevant parties of compliance
- Reviews restrictions annually or upon court order update

### Vulnerable Learners
For learners with identified vulnerabilities (e.g., special educational needs, safeguarding concerns):
- Additional consent options may be presented
- Safeguarding Board may require enhanced protections
- Individualized consent plan created
- Regular review and adjustment

### Transitional Consent (Age-Tier Changes)
When a learner transitions to a new age tier:
- Parents/guardians notified in advance
- New tier implications explained
- Consent automatically reviewed
- Option to adjust consent categories

---

## Data and Privacy

All consent data is:

- **Minimal:** Only essential information collected
- **Secure:** Industry-standard encryption and storage
- **Non-commercial:** Never sold or shared for profit
- **Transparent:** Families can view their consent records
- **Revocable:** Deleted upon withdrawal (subject to legal retention)

See Privacy Policy and Data Protection frameworks for full details.

---

## Constitutional Authority

This consent flow operates under:

- The Virtual Centre Licensing Agreement
- The Safeguarding Board mandate
- The Foundational Principles
- The Soft Guardrail Philosophy

All consent decisions are subject to institutional governance and safeguarding oversight.

---

## Questions and Support

For consent questions or support:

- **Technical issues:** Contact institutional support
- **Consent guidance:** Licensing & Civic Agreements body
- **Safeguarding concerns:** Safeguarding Board
- **General inquiries:** Institutional stewards

---

**Consent is a promise of respect.**  
**Consent is a protection of autonomy.**  
**Consent is held in trust for the families we serve.**
