# Developer Onboarding Guide

Welcome to the platform. This guide provides the essential steps to begin contributing with clarity and confidence.

---

## 1. Principles to Understand First
The platform is built on:
- Honesty
- Integrity
- Trust
- Protection
- Culture

Every commit should reflect these values.

---

## 2. Repository Structure
See `STRUCTURE.md` and `/docs/technical/architecture.md` for full details.

Key areas:
- `/backend` — core services, contracts, protection logic
- `/frontend` — UI, components, flows
- `/docs` — brand, platform, technical, legal
- `/tests` — backend and frontend tests

---

## 3. Setup

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git
- Docker (optional, for local development)

### Backend Setup
```bash
# Clone the repository
git clone https://github.com/Fitzroy02/John-T-Hope-app.git
cd John-T-Hope-app

# Install backend dependencies
pip install -r requirements.txt

# Run backend tests
pytest backend/tests/

# Start backend server
python backend/app.py
```

### Frontend Setup
```bash
# Install frontend dependencies
cd frontend
npm install

# Run frontend development server
npm run dev

# Run frontend tests
npm test
```

---

## 4. Development Workflow

### Branching Strategy
- `main` — production-ready code
- `develop` — integration branch for features
- `feature/[name]` — individual feature branches
- `fix/[name]` — bug fix branches

### Commit Message Format
We follow conventional commit standards:
- `feat:` — new features
- `fix:` — bug fixes
- `docs:` — documentation changes
- `refactor:` — code refactoring
- `test:` — test additions or modifications
- `chore:` — maintenance tasks

Example:
```
feat: add contract verification service
fix: resolve payment processing timeout
docs: update API specification
```

---

## 5. Code Standards

### Backend (Python)
- Follow PEP 8 style guide
- Use type hints
- Write docstrings for all functions
- Keep functions small and focused
- Test coverage should be >80%

### Frontend (JavaScript/TypeScript)
- Use ESLint and Prettier
- Follow component-based architecture
- Write meaningful component names
- Keep components focused on single responsibility
- Write unit tests for all components

---

## 6. Key Concepts

### Platform Protection
- Every eligible transaction includes Platform Protection
- Protection is funded through the Platform Service Fee
- The platform is **not** an insurer
- Claims are handled by a third-party insurer

### Contract System
- Contracts are the core of every transaction
- Contracts must be clear, enforceable, and user-friendly
- Both parties must explicitly agree to terms

### Cultural Logic
- Region-first approach
- Selector-led discovery
- Scene-aware recommendations
- Respect for cultural context

---

## 7. Documentation Requirements

Before submitting a pull request:
- Update relevant documentation in `/docs`
- Add inline code comments for complex logic
- Update API specifications if endpoints change
- Add examples for new features

---

## 8. Testing

### Backend Testing
```bash
# Run all backend tests
pytest backend/tests/

# Run specific test file
pytest backend/tests/test_contracts.py

# Run with coverage
pytest --cov=backend backend/tests/
```

### Frontend Testing
```bash
# Run all frontend tests
npm test

# Run tests in watch mode
npm test -- --watch

# Run with coverage
npm test -- --coverage
```

---

## 9. Pull Request Process

1. **Create a feature branch** from `develop`
2. **Implement your changes** following code standards
3. **Write tests** for new functionality
4. **Update documentation** as needed
5. **Run all tests** to ensure nothing breaks
6. **Commit with clear messages** using conventional format
7. **Push to your branch** and open a pull request
8. **Request review** from maintainers
9. **Address feedback** and make requested changes
10. **Merge** once approved

### Pull Request Template
```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Performance improvement

## Testing
Describe how this was tested.

## Checklist
- [ ] Code follows project standards
- [ ] Tests pass locally
- [ ] Documentation updated
- [ ] No breaking changes (or documented if necessary)
```

---

## 10. Getting Help

### Documentation
- [Architecture Overview](./architecture.md)
- [API Specification](./api-spec.md)
- [Data Models](./data-models.md)
- [Brand Voice Guide](../brand/brand-voice.md)

### Communication
- Open an issue for bugs or feature requests
- Ask questions in pull request comments
- Tag maintainers for urgent matters

---

## 11. What Not to Do

❌ **Don't** bypass protection logic  
❌ **Don't** store sensitive data without encryption  
❌ **Don't** commit directly to `main`  
❌ **Don't** use hype language or corporate clichés  
❌ **Don't** compromise on code quality for speed  
❌ **Don't** skip writing tests  
❌ **Don't** merge without review  

---

## 12. Cultural Considerations

This platform serves creative and cultural workers. When developing:
- Respect the language of culture (DJs, selectors, promoters, venues)
- Design for professionalism and dignity
- Keep cultural context in mind
- Test with real-world scenarios
- Listen to user feedback from the community

---

## 13. Security Guidelines

- Never commit API keys or secrets
- Use environment variables for configuration
- Validate all user input
- Implement proper authentication and authorization
- Keep dependencies updated
- Report security vulnerabilities privately

---

## 14. Performance Considerations

- Optimize database queries
- Implement caching where appropriate
- Minimize API calls
- Lazy load components when possible
- Monitor performance metrics

---

## 15. Accessibility Standards

- Follow WCAG 2.1 AA guidelines
- Use semantic HTML
- Provide alt text for images
- Ensure keyboard navigation
- Test with screen readers

---

**Welcome to the team. Build with integrity. Code with clarity.**