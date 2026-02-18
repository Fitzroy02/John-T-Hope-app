# Consent Integration

**Implementation Guide for Parental Consent in Healthcare Content**

---

## Purpose

This guide provides practical implementation for parental consent systems in healthcare content delivery, balancing legal requirements, developmental appropriateness, and child autonomy.

---

## Core Principles

### 1. Legal Compliance
Parental consent requirements vary dramatically by jurisdiction. All implementations must comply with local law.

### 2. Developmental Appropriateness
Consent requirements should align with developmental stages and healthcare autonomy.

### 3. Respect for Evolving Capacity
As children mature, their capacity for autonomous healthcare decisions grows. Systems should acknowledge this.

### 4. Safeguarding Balance
Parental involvement is important, but absolute parental control can prevent vulnerable children from accessing necessary health information or support.

### 5. Privacy and Trust
Excessive parental surveillance can discourage honest health information seeking. Balance transparency with privacy.

---

## Consent Tiers

Healthcare content requires different consent levels based on age, topic, and jurisdiction.

---

## Tier 1: No Parental Consent Required

### When Applied
- Low-risk, general health content
- Age-appropriate content for all tiers
- Jurisdictions with low consent requirements

### Examples
- General health awareness content
- Basic body literacy
- Universal wellness content

### Rationale
Content is non-sensitive, age-appropriate, and widely accepted as suitable for all ages.

### Implementation
- No consent flow
- Standard age verification only
- Parental access to view content available

---

## Tier 2: Parental Notification (Optional)

### When Applied
- Moderate-risk content
- Body development content
- Jurisdictions with notification preferences

### Examples
- Puberty education
- Basic reproductive health literacy
- Mental health awareness

### Rationale
Parents may want to know their child is accessing this content but legal consent is not required.

### Implementation
- Parental notification sent (if parent account linked)
- Content access not blocked
- Parent can view content their child accessed
- Parent can opt-in to notifications

### Notification Example
"Your child accessed puberty education content. You can review the content here: [link]. This is age-appropriate educational content."

---

## Tier 3: Parental Consent Required (Soft)

### When Applied
- Moderate-to-high risk content
- Younger users accessing sensitive content
- Jurisdictions with consent preferences but not legal mandate

### Examples
- Detailed sexual health content for younger teens (13-15)
- Mental health condition literacy
- Substance use awareness

### Rationale
Content is sensitive enough to warrant parental awareness and approval, though not legally mandated.

### Implementation
- Consent request sent to parent
- Content blocked until consent given OR
- Limited version provided until consent given
- Clear timeline for parent response
- Escalation path if parent doesn't respond

### Consent Request Example
"Your child has requested access to [content category]. This content is age-appropriate but sensitive. Please review the content description and approve or decline access. [Description] [Approve] [Decline] [View Sample Content]"

---

## Tier 4: Parental Consent Required (Hard)

### When Applied
- High-risk content
- Younger users (below age of medical consent)
- Jurisdictions with legal consent requirements

### Examples
- Sexual health content below age of consent
- Gender-affirming healthcare information (jurisdiction-dependent)
- Reproductive health information (jurisdiction-dependent)

### Rationale
Legal requirement or strong ethical obligation for parental involvement.

### Implementation
- Mandatory consent before access
- No content provided without consent
- Clear explanation to both child and parent
- Alternative support pathways for children in unsafe home situations
- Safeguarding considerations paramount

### Consent Request Example
"Your child has requested access to [content]. Due to legal requirements in [country], parental consent is required. Please review this information and approve or decline. [Full description] [Legal context] [Approve] [Decline]"

---

## Special Case: Consent and Safeguarding

### The Dilemma
Sometimes parental consent requirements conflict with safeguarding needs. Example: A child in an abusive home needs mental health or sexual health information but parent would deny consent or retaliate.

### Approach

**Priority**: Safeguarding trumps consent requirements where conflict exists.

**Implementation**:
1. Where possible, provide general information that doesn't require consent
2. Ensure crisis resources are always available without consent
3. Provide pathways to professional support (school counselors, healthcare providers, safeguarding services) that can bypass parental consent where legally permitted
4. Never block access to crisis resources
5. Document decisions to override consent requirements with safeguarding justification

**Example**:
- Crisis resources for abuse, self-harm, suicide: Always available, no consent required
- General mental health literacy: Available without consent
- Detailed mental health condition information: May require consent, but crisis resources never blocked

---

## Jurisdiction-Specific Implementation

### Research Required for Each Jurisdiction
- Age of medical consent
- Parental consent requirements for health information
- "Mature minor" doctrine existence and application
- Exceptions for crisis situations
- Mandatory reporting obligations

### Country Profile Integration
Country profiles (see `COUNTRY_PROFILES_LEGAL_VARIATION.md`) document consent requirements per jurisdiction.

**Technical Implementation**: 
- User location determines consent tier requirements
- Geolocation-based consent flows
- Country-specific consent language

---

## Consent Workflow Design

### Step 1: User Requests Access
User attempts to access healthcare content requiring consent.

### Step 2: Consent Check
System checks:
- User age tier
- Content risk level
- Jurisdiction consent requirements
- Existing consent status

### Step 3: Consent Requirement Determination
System determines:
- No consent needed → Grant access
- Notification only → Grant access, notify parent
- Soft consent → Request consent, provide limited access or wait
- Hard consent → Request consent, block access until granted

### Step 4: Parent Notification/Request
Parent receives notification or consent request via:
- Email (if parent account linked)
- In-app notification (if parent has account)
- SMS (if configured)

### Step 5: Parent Review
Parent reviews:
- Content description
- Why child is requesting
- Sample content (where appropriate)
- Educational rationale

### Step 6: Parent Decision
Parent:
- Approves → Access granted
- Declines → Access denied, alternative resources offered
- Doesn't respond → Escalation (soft consent) or continued block (hard consent)

### Step 7: User Notification
User notified of outcome:
- Approval → Access granted with positive message
- Decline → Alternative resources provided, explanation given
- Pending → Waiting message, timeline provided

---

## Consent Management

### Consent Tracking
System tracks:
- Consent requests sent
- Consent decisions made
- Consent expiry (for time-limited consent)
- Consent revocation

### Consent Granularity
Parents can consent to:
- Specific content items
- Content categories
- All content in a tier
- Time-limited access

### Consent Revocation
Parents can revoke consent at any time.
- Immediate effect
- User notified
- Alternative resources provided

### Consent Expiry
For evolving topics or temporary consent, expiry dates can be set.
- Consent expires after set period
- Renewal request sent to parent
- User notified before expiry

---

## User Communication

### To Children/Adolescents

**When Consent Required**:
"Some health topics require parent or guardian permission for people under [age]. We've sent a request to your parent. This is normal and helps make sure you get the right information at the right time."

**When Consent Denied**:
"Your parent has chosen not to provide access to this content right now. This doesn't mean your questions aren't important. Here are some other resources: [links]. You can also talk to a trusted adult like a school counselor or healthcare provider."

**When Consent Delayed**:
"We're waiting for your parent to review the request. This usually takes [timeframe]. In the meantime, here are some related resources: [links]."

---

### To Parents

**Consent Request**:
"Your child is seeking health information about [topic]. This is a natural part of growing up and learning about their body and health. The content is educational, age-appropriate, and evidence-based. Please review and decide whether to provide access."

**Educational Framing**:
"Health literacy is important for young people. This content helps your child understand [topic] in an age-appropriate, safe way."

**Reassurance**:
"All healthcare content is non-diagnostic, non-prescriptive, and evidence-based. We never provide medical advice. Content is designed to encourage young people to talk to trusted adults and healthcare providers."

---

## Alternative Pathways

### For Users Without Parent Access
Some users may not have:
- Parents available
- Safe home environment
- Parent willing to engage with system

**Solutions**:
1. **Guardian Alternative**: Allow other guardians (grandparents, foster parents, etc.) to provide consent
2. **Professional Support**: Direct to school counselors, healthcare providers who can provide information directly
3. **Age-Appropriate General Content**: Provide general information that doesn't require consent
4. **Crisis Resources**: Always available regardless of consent status

---

## Technical Implementation

### Parent Account Linking
- Users can link parent accounts during signup or later
- Parent verifies relationship
- Parent sets consent preferences

### Consent Dashboard
Parents access dashboard showing:
- Child's content access requests
- Pending consent decisions
- Approved/denied history
- Ability to review content child has accessed
- Consent management tools

### Child Dashboard
Children see:
- Consent status of requested content
- Alternative resources while waiting
- Ability to request consent
- Understanding of why consent required

### Automated Consent Flows
- Email/SMS notifications
- In-app notifications
- Reminder sequences (for pending consents)
- Expiry warnings

---

## Governance Oversight

### Consent System Audits
Regular audits of:
- Consent request patterns
- Approval/denial rates
- Response times
- User feedback on consent system
- Safeguarding incidents related to consent

### Policy Review
Consent policies reviewed:
- Annually
- When entering new jurisdictions
- When legal frameworks change
- When user feedback indicates problems

### Safeguarding Integration Review
Regular review of:
- Situations where consent blocked vulnerable users from help
- Situations where lack of consent raised safeguarding concerns
- Balance between consent and safeguarding

---

## Edge Cases

### Divorced/Separated Parents
- Both parents can be linked
- Either parent can provide consent (unless legal restrictions exist)
- Conflicting decisions escalated to governance team

### Foster Care
- Foster parents treated as guardians
- Social workers can provide consent where appropriate
- System flexible to complex family situations

### International Families
- Geolocation determines consent requirements
- User's current location, not parent's, determines rules
- Complex situations escalated to governance team

### Age Boundary Transitions
- When user reaches age of medical consent, consent requirements automatically adjust
- Parents notified of transition
- User retains access to previously accessed content

---

## Related Documents

- `COUNTRY_PROFILES_LEGAL_VARIATION.md` - Jurisdiction-specific consent requirements
- `AGE_TIERED_HEALTHCARE_LEARNING.md` - Age-appropriate content
- `SAFEGUARDING_INTEGRATION.md` - Safeguarding protocols
- `HEALTHCARE_GOVERNANCE_PRINCIPLES.md` - Foundational principles

---

**Last Updated**: 2026-02-18  
**Next Review**: 2027-02-18  
**Document Owner**: Governance Lead  
**Version**: 1.0
