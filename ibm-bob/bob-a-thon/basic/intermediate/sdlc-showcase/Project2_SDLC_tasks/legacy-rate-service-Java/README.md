# Legacy Rate Service

## ⚠️ WARNING: This is Legacy Code for Demonstration Purposes

This service contains **intentional legacy code anti-patterns** for demonstrating Bob's code modernization capabilities.

## 🎯 Purpose

This legacy banking rate service demonstrates common issues found in older enterprise Java applications:

### Legacy Issues Present:

1. **Java 8** - Outdated Java version (current is Java 21)
2. **Synchronous Blocking Calls** - No async/reactive programming
3. **No Connection Pooling** - Creates new DB connection for every request
4. **Deprecated Libraries** - Apache Commons HttpClient 3.x, Commons Lang 2.x
5. **No Structured Logging** - Uses `System.out.println` instead of proper logging
6. **Try-Catch Soup** - Excessive nested try-catch blocks making code unreadable
7. **SQL Injection Vulnerabilities** - Non-parameterized queries
8. **No Transaction Management** - Database operations without proper transactions
9. **Performance Bottlenecks** - Inefficient algorithms and blocking operations
10. **Poor Error Handling** - Generic exception catching and swallowing

## 📋 Functionality

The service provides banking account rate information:

- **Get All Account Rates** - Retrieves rates for all account types (checking, savings, money market)
- **Get Rate by Account Type** - Looks up rate for specific account type
- **Fetch Market Rates** - Retrieves current market rates from external API
- **Update Account Rate** - Updates rate for specific account type
- **Calculate Compound Interest** - Calculates compound interest over time

## 🏗️ Architecture Issues

### Database Layer
- ❌ No connection pooling (creates new connection each time)
- ❌ No prepared statements (SQL injection risk)
- ❌ No transaction management
- ❌ Manual resource cleanup (error-prone)

### HTTP Client
- ❌ Using deprecated Apache Commons HttpClient 3.x
- ❌ Synchronous blocking calls
- ❌ No timeout configuration
- ❌ No retry logic

### Logging
- ❌ Using `System.out.println` instead of logging framework
- ❌ No log levels (DEBUG, INFO, WARN, ERROR)
- ❌ No structured logging
- ❌ No correlation IDs for tracing

### Error Handling
- ❌ Excessive nested try-catch blocks
- ❌ Generic exception catching
- ❌ Swallowing exceptions
- ❌ Poor error messages

### Code Quality
- ❌ No use of modern Java features (streams, lambdas, Optional)
- ❌ Verbose boilerplate code
- ❌ Poor separation of concerns
- ❌ No dependency injection

## 🔧 Build Instructions

```bash
# Build the project
cd legacy-rate-service
mvn clean package

# Run tests
mvn test

# Generate dependency report (shows deprecated libraries)
mvn dependency:tree
```

## 📊 Modernization Opportunities

### Recommended Improvements:

1. **Upgrade to Java 21**
   - Use records for data classes
   - Use pattern matching
   - Use text blocks
   - Use sealed classes

2. **Implement Connection Pooling**
   - Use HikariCP for database connections
   - Configure proper pool sizes
   - Add connection validation

3. **Replace Deprecated Libraries**
   - Apache HttpClient 3.x → HttpClient 5.x or WebClient
   - Commons Lang 2.x → Commons Lang 3.x
   - Add SLF4J + Logback for logging

4. **Add Structured Logging**
   - Replace System.out.println with proper logger
   - Add log levels
   - Add correlation IDs
   - Use structured logging (JSON)

5. **Implement Async/Reactive**
   - Use CompletableFuture for async operations
   - Consider Spring WebFlux for reactive programming
   - Use non-blocking I/O

6. **Improve Error Handling**
   - Use try-with-resources for auto-cleanup
   - Create custom exception hierarchy
   - Add proper error messages
   - Implement circuit breakers

7. **Add Security**
   - Use prepared statements (prevent SQL injection)
   - Add input validation
   - Implement authentication/authorization
   - Encrypt sensitive data

8. **Performance Optimization**
   - Add caching (Redis, Caffeine)
   - Implement batch operations
   - Use parallel streams where appropriate
   - Add database indexes

## 🎓 Demo Usage

This code is designed for demonstrating Bob's modernization capabilities:

1. **Analysis Phase** - Bob identifies all legacy patterns and issues
2. **Planning Phase** - Bob creates modernization roadmap
3. **Refactoring Phase** - Bob applies modern patterns and best practices
4. **Validation Phase** - Bob ensures functionality is preserved

See `docs/demos/USE_CASE_2_LEGACY_MODERNIZATION.md` for complete demo guide.

## ⚠️ Do Not Use in Production

This code contains intentional anti-patterns and should **never** be used in production environments.

## 📚 Related Documentation

- [Demo Guide](../docs/demos/USE_CASE_2_LEGACY_MODERNIZATION.md)
- [Executive Summary](../docs/demos/USE_CASE_2_EXECUTIVE_SUMMARY.md)
- [Modernization Best Practices](../docs/reference/MODERNIZATION_BEST_PRACTICES.md)

---

**Created for**: Bob AI Coding Assistant Demo  
**Purpose**: Legacy Code Modernization Use Case  
**Status**: Intentionally Legacy - For Demo Only