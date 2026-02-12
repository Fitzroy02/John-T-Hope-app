# Repository Structure

**Clean. Scalable. Future-proof.**

---

## Overview

This repository is organized to support a professional, protected transaction platform for creative and cultural workers. The structure reflects our core principles: honesty, integrity, trust, protection, and culture.

---

## Folder Layout

```
/
├── backend/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── controllers/
│   ├── contracts/
│   ├── protection/
│   ├── utils/
│   └── tests/
│
├── frontend/
│   ├── components/
│   ├── pages/
│   ├── hooks/
│   ├── styles/
│   ├── context/
│   └── utils/
│
├── docs/
│   ├── brand/
│   │   ├── brand-voice.md
│   │   ├── tagline-system.md
│   │   └── messaging-guide.md
│   ├── platform/
│   │   ├── admin-fee-table.md
│   │   ├── protection-model.md
│   │   ├── user-journeys.md
│   │   └── cultural-logic.md
│   ├── technical/
│   │   ├── architecture.md
│   │   ├── api-spec.md
│   │   ├── data-models.md
│   │   └── dev-onboarding.md
│   └── legal/
│       ├── terms-outline.md
│       ├── privacy-outline.md
│       └── compliance-notes.md
│
├── scripts/
│   ├── setup/
│   ├── deployment/
│   └── utilities/
│
├── tests/
│   ├── backend/
│   └── frontend/
│
├── .gitignore
├── package.json
├── README.md
├── STRUCTURE.md
└── LICENSE
```

---

## Directory Descriptions

### `/backend`
Core server-side logic and services.

#### `/backend/api`
API endpoints and route handlers.

#### `/backend/services`
Business logic layer (user service, contract service, protection service, etc.).

#### `/backend/models`
Database models and schemas.

#### `/backend/controllers`
Request/response handling and validation.

#### `/backend/contracts`
Contract generation, storage, and management logic.

#### `/backend/protection`
Platform Protection eligibility checks, insurance integration, claim routing.

#### `/backend/utils`
Helper functions and shared utilities.

#### `/backend/tests`
Backend unit and integration tests.

---

### `/frontend`
User interface components and pages.

#### `/frontend/components`
Reusable UI components (buttons, forms, cards, modals, etc.).

#### `/frontend/pages`
Page-level components (home, profile, contracts, dashboard, etc.).

#### `/frontend/hooks`
Custom React hooks for state management and side effects.

#### `/frontend/styles`
Global styles, themes, and design tokens.

#### `/frontend/context`
React context providers for global state (auth, user, theme, etc.).

#### `/frontend/utils`
Frontend helper functions and utilities.

---

### `/docs`
Comprehensive documentation for brand, platform, technical, and legal matters.

#### `/docs/brand`
Brand voice guidelines, tagline system, messaging frameworks.

#### `/docs/platform`
Platform logic, fee structure, protection model, user journeys, cultural algorithms.

#### `/docs/technical`
Architecture diagrams, API specifications, data models, developer onboarding.

#### `/docs/legal`
Terms of service outlines, privacy policy drafts, compliance notes.

---

### `/scripts`
Automation scripts for setup, deployment, and maintenance.

#### `/scripts/setup`
Environment setup, dependency installation, database initialization.

#### `/scripts/deployment`
Build and deployment automation.

#### `/scripts/utilities`
Database migrations, data seeding, backup scripts.

---

### `/tests`
Test suites organized by application layer.

#### `/tests/backend`
Backend test suites.

#### `/tests/frontend`
Frontend test suites.

---

## Current Status

### Implemented
- ✅ Documentation structure (`/docs`)
- ✅ Brand voice guide
- ✅ Platform Protection documentation
- ✅ Fee structure documentation
- ✅ User-facing terms
- ✅ Homepage copy
- ✅ Investor deck content
- ✅ README and STRUCTURE files

### In Progress
- 🔄 Backend service architecture
- 🔄 Frontend component library
- 🔄 Database schema design

### Planned
- 📋 API implementation
- 📋 Contract generation system
- 📋 Platform Protection integration
- 📋 User authentication and verification
- 📋 Payment processing
- 📋 Cultural logic engine

---

## Contributing

When adding new files or folders:

1. Follow the established structure
2. Keep related code together
3. Document new directories in this file
4. Use clear, descriptive names
5. Maintain separation of concerns

---

## Principles

### Clarity
Every folder and file has a clear purpose.

### Scalability
The structure supports growth without reorganization.

### Separation of Concerns
Backend, frontend, documentation, and scripts are cleanly separated.

### Cultural Integrity
The structure reflects the platform's values and purpose.

---

**This structure is intentional. This structure is our foundation.**