# Data Models — High-Level

This document outlines the core data structures used across the platform.

---

## User

- id
- name
- email
- role (DJ, promoter, venue, client)
- verification_status
- region
- genres
- reputation_score
- created_at
- updated_at

---

## Profile

- user_id
- bio
- skills
- cultural_history
- media_links
- availability

---

## Contract

- id
- creator_id
- participant_id
- terms
- date
- fee
- status (draft, signed, completed)
- protection_eligible (boolean)
- created_at
- updated_at

---

## Transaction

- id
- contract_id
- amount
- platform_fee
- payout_amount
- status (pending, paid, disputed)
- created_at

---

## Protection Claim

- id
- transaction_id
- user_id
- reason
- status (submitted, under_review, accepted, rejected)
- insurer_reference
- created_at

---

## Cultural Metadata

### Region
- id
- name
- description

### Genre
- id
- name
- parent_genre
- cultural_notes

---

## Messaging

- id
- sender_id
- receiver_id
- content
- timestamp

---

**Data structured with integrity. Models you can trust.**