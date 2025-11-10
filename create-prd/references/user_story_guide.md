# User Story Writing Guide

## What is a User Story?

A user story is a short, simple description of a feature told from the perspective of the user. It focuses on the value a feature brings to the user rather than technical implementation details.

## User Story Format

### Classic Format
```
As a [type of user]
I want to [perform some action]
So that I can [achieve some goal/benefit]
```

### Examples
- As a **podcast listener**, I want to **save episodes for offline listening** so that I can **enjoy content without internet connection**
- As a **team manager**, I want to **see my team's progress dashboard** so that I can **identify bottlenecks quickly**
- As a **marketplace seller**, I want to **bulk upload products** so that I can **list inventory efficiently**

## INVEST Criteria

Every good user story should be:

### Independent
- Can be developed and delivered separately
- Minimal dependencies on other stories
- Can be reordered in the backlog

### Negotiable
- Not a contract, but a conversation starter
- Details emerge through discussion
- Implementation is flexible

### Valuable
- Delivers value to end users or customers
- Has clear benefit
- Solves a real problem

### Estimable
- Team can estimate the effort
- Enough detail to understand scope
- Risks are identified

### Small
- Fits in one sprint/iteration
- Can be completed by one developer/pair
- 1-5 days of work ideal

### Testable
- Clear acceptance criteria
- Definable done state
- Can be demonstrated

## Writing Effective User Stories

### Focus on User Goals, Not Features
❌ Bad: "Add a search bar to the page"
✅ Good: "As a user, I want to search for products so that I can find what I need quickly"

### Be Specific About the User
❌ Bad: "As a user..."
✅ Good: "As a first-time visitor..." or "As a premium subscriber..."

### Emphasize the Value
❌ Bad: "...so that I can see the data"
✅ Good: "...so that I can make informed decisions about inventory"

### Keep It Simple
❌ Bad: Complex multi-paragraph story
✅ Good: One sentence that captures the essence

## Acceptance Criteria

### What Are Acceptance Criteria?
Conditions that must be met for the story to be considered complete.

### Format Options

#### Scenario Format (Given-When-Then)
```
GIVEN [initial context]
WHEN [action occurs]
THEN [expected outcome]
```

Example:
```
GIVEN I am on the login page
WHEN I enter valid credentials
THEN I should be redirected to my dashboard
```

#### Checklist Format
- [ ] User can enter email and password
- [ ] System validates credentials
- [ ] Success redirects to dashboard
- [ ] Failure shows error message
- [ ] Password is masked during entry

#### Rule-Based Format
- Must accept email format only
- Password minimum 8 characters
- Show error for invalid credentials
- Lock after 5 failed attempts
- Remember me option available

## User Story Patterns

### CRUD Operations
```
Create: As a [user], I want to create [item] so that [benefit]
Read: As a [user], I want to view [item] so that [benefit]
Update: As a [user], I want to edit [item] so that [benefit]
Delete: As a [user], I want to remove [item] so that [benefit]
```

### Search and Filter
```
As a [user], I want to search for [items] by [criteria] so that I can find [specific items] quickly
As a [user], I want to filter [items] by [attribute] so that I can see only relevant results
```

### Authentication
```
As a new visitor, I want to create an account so that I can save my preferences
As a registered user, I want to log in so that I can access my personal data
As a logged-in user, I want to log out so that I can secure my account
```

### Notifications
```
As a [user], I want to receive [notification type] when [event] so that I can [take action]
As a [user], I want to manage my notification preferences so that I only get relevant updates
```

## Breaking Down Large Stories (Epics)

### Vertical Slicing
Split by user journey completion:
1. Basic happy path
2. Alternative paths
3. Error handling
4. Edge cases

### Horizontal Slicing (Avoid When Possible)
Split by technical layer:
- UI only
- Backend only
- Database only

### SPIDR Method
- **Spike**: Research story
- **Path**: Different user paths
- **Interface**: Different UI elements
- **Data**: Different data types
- **Rules**: Different business rules

## Common Mistakes to Avoid

### Technical Stories
❌ "As a developer, I want to refactor the database..."
✅ Frame in user value or create a technical task

### Vague Benefits
❌ "...so that it works better"
✅ "...so that page loads 50% faster"

### Multiple Stories in One
❌ "As a user, I want to login, see dashboard, and export data..."
✅ Split into separate stories

### Solution in Disguise
❌ "As a user, I want a dropdown menu..."
✅ "As a user, I want to select from available options..."

## Story Sizing

### T-Shirt Sizes
- **XS**: Few hours
- **S**: 1-2 days
- **M**: 3-5 days
- **L**: 1-2 weeks (should split)
- **XL**: 2+ weeks (must split)

### Story Points
- 1-2: Trivial change
- 3-5: Simple feature
- 8-13: Complex feature
- 20+: Epic, needs splitting

## Definition of Done

### Story Level
- [ ] Code complete
- [ ] Unit tests written
- [ ] Code reviewed
- [ ] Acceptance criteria met
- [ ] Documentation updated
- [ ] Deployed to staging

### Feature Level
- [ ] All stories complete
- [ ] Integration tested
- [ ] Performance acceptable
- [ ] Security reviewed
- [ ] Product owner approved
- [ ] Released to production

## Story Lifecycle

1. **Draft**: Initial idea captured
2. **Refined**: Details added, acceptance criteria defined
3. **Estimated**: Team agrees on effort
4. **Committed**: Pulled into sprint
5. **In Progress**: Being developed
6. **Testing**: Verification against criteria
7. **Done**: All criteria met
8. **Accepted**: Product owner approved

## Templates and Examples

### Basic Feature Story
```
Title: User Registration

As a new visitor
I want to create an account with my email
So that I can save my preferences and history

Acceptance Criteria:
- Email must be unique
- Password min 8 characters
- Confirmation email sent
- Auto-login after registration
```

### API Integration Story
```
Title: Payment Processing

As a customer
I want to pay with credit card
So that I can complete my purchase

Acceptance Criteria:
- Supports Visa, Mastercard, Amex
- PCI compliant
- Handles success and failure
- Saves transaction record
- Sends receipt email
```

### Performance Story
```
Title: Fast Search Results

As a user searching for products
I want to see results within 2 seconds
So that I can quickly find what I need

Acceptance Criteria:
- 95% of searches < 2 seconds
- Shows loading indicator
- Handles 1000+ concurrent users
- Caches common searches
```

## Quick Reference

### Story Template
```
As a [persona]
I want to [action]
So that I can [benefit]

Acceptance Criteria:
- [Specific condition 1]
- [Specific condition 2]
- [Specific condition 3]
```

### Checklist for Good Stories
- [ ] Follows As a/I want/So that format
- [ ] Specific user type identified
- [ ] Clear value stated
- [ ] Acceptance criteria defined
- [ ] INVEST criteria met
- [ ] Can be done in one sprint
- [ ] Testable outcome

### Questions to Ask
1. Who is the user?
2. What problem does this solve?
3. What's the simplest solution?
4. How will we know it works?
5. What could go wrong?
6. Is this the right size?
