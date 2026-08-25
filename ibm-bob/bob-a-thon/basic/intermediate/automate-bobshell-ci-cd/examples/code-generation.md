# BobShellコード生成例

## 概要

このドキュメントは、自然言語プロンプトを使用したBobShellによるコード生成の包括的な例を提供します。 様々なプログラミング言語、フレームワーク、ユースケースに対して高品質なコードを生成する方法を学びます。

## 目次

1. [基本的なコード生成](#基本的なコード生成)
2. [Web開発](#web開発)
3. [バックエンド開発](#バックエンド開発)
4. [データベース操作](#データベース操作)
5. [テスト](#テスト)
6. [ユーティリティとヘルパー](#ユーティリティとヘルパー)
7. [高度なパターン](#高度なパターン)

## 基本的なコード生成

### シンプルな関数

```bash
# Generate a sorting function
bob "Create a Python function to sort a list of dictionaries by a specific key" --yolo --hide-intermediary-output > sort_dicts.py

# Generate a validation function
bob "Create a JavaScript function to validate email addresses with regex" --yolo --hide-intermediary-output > validate-email.js

# Generate a utility function
bob "Create a TypeScript function to debounce function calls" --yolo --hide-intermediary-output > debounce.ts
```

### クラスとオブジェクト

```bash
# Generate a Python class
bob "Create a Python class for a shopping cart with methods to add items, remove items, calculate total, and apply discounts" > shopping_cart.py

# Generate a JavaScript class
bob "Create a JavaScript ES6 class for managing user sessions with login, logout, and session validation" > SessionManager.js

# Generate a TypeScript interface
bob "Create TypeScript interfaces for a blog post with author, content, tags, and metadata" > blog-types.ts
```

### データ構造

```bash
# Generate a linked list implementation
bob "Create a Python implementation of a doubly linked list with insert, delete, and search methods" --yolo --hide-intermediary-output > linked_list.py

# Generate a binary tree
bob "Create a JavaScript binary search tree with insert, search, and traversal methods" --yolo --hide-intermediary-output > binary-tree.js

# Generate a graph structure
bob "Create a Python graph data structure with adjacency list representation and BFS/DFS traversal" --yolo --hide-intermediary-output > graph.py
```

## Web開発

### Reactコンポーネント

```bash
# Generate a functional component
bob "Create a React functional component for a user profile card with avatar, name, bio, and social links using hooks" --yolo --hide-intermediary-output > UserProfile.jsx

# Generate a form component
bob "Create a React form component for user registration with email, password, validation, and error handling" --yolo --hide-intermediary-output > RegistrationForm.jsx

# Generate a data table component
bob "Create a React component for a sortable, filterable data table with pagination" --yolo --hide-intermediary-output > DataTable.jsx

# Generate with TypeScript
bob "Create a TypeScript React component for a todo list with add, delete, and toggle complete functionality" --yolo --hide-intermediary-output > TodoList.tsx
```

### Vueコンポーネント

```bash
# Generate Vue 3 component
bob "Create a Vue 3 component for a product card with image, title, price, and add to cart button using Composition API" --yolo --hide-intermediary-output > ProductCard.vue

# Generate with script setup
bob "Create a Vue 3 component using script setup for a search bar with debounced input and suggestions" --yolo --hide-intermediary-output > SearchBar.vue
```

### Angularコンポーネント

```bash
# Generate Angular component
bob "Create an Angular component for a navigation menu with routing and active state highlighting" --yolo --hide-intermediary-output > navigation.component.ts

# Generate with service
bob "Create an Angular component with a service for fetching and displaying user data"
```

### HTML/CSS

```bash
# Generate HTML structure
bob "Create an HTML5 structure for a landing page with header, hero section, features, and footer" --yolo --hide-intermediary-output > landing.html

# Generate CSS styles
bob "Create CSS styles for a responsive card layout with hover effects and animations" --yolo --hide-intermediary-output > card-styles.css

# Generate with Tailwind
bob "Create HTML with Tailwind CSS classes for a modern dashboard layout" --yolo --hide-intermediary-output > dashboard.html
```

## バックエンド開発

### Express.js API

```bash
# Generate REST API endpoint
bob "Create an Express.js REST API endpoint for user CRUD operations with validation and error handling" --yolo --hide-intermediary-output > users-routes.js

# Generate middleware
bob "Create Express.js middleware for JWT authentication with token validation and refresh" --yolo --hide-intermediary-output > auth-middleware.js

# Generate complete API
bob "Create a complete Express.js API for a blog with posts, comments, and authentication"
```

### Flask API

```bash
# Generate Flask route
bob "Create a Flask route for user authentication with login, logout, and token generation" --yolo --hide-intermediary-output > auth_routes.py

# Generate Flask blueprint
bob "Create a Flask blueprint for a products API with CRUD operations and pagination" --yolo --hide-intermediary-output > products_blueprint.py

# Generate with SQLAlchemy
bob "Create Flask routes with SQLAlchemy models for a task management system"
```

### FastAPI

```bash
# Generate FastAPI endpoint
bob "Create a FastAPI endpoint for file upload with validation and storage" --yolo --hide-intermediary-output > upload_endpoint.py

# Generate with Pydantic models
bob "Create FastAPI endpoints with Pydantic models for a user management system" --yolo --hide-intermediary-output > user_api.py

# Generate async endpoints
bob "Create async FastAPI endpoints for a real-time chat application" --yolo --hide-intermediary-output > chat_api.py
```

### GraphQL

```bash
# Generate GraphQL schema
bob "Create a GraphQL schema for a social media application with users, posts, and comments" --yolo --hide-intermediary-output > schema.graphql

# Generate resolvers
bob "Create GraphQL resolvers for the social media schema with database queries" --yolo --hide-intermediary-output > resolvers.js
```

## データベース操作

### SQLクエリ

```bash
# Generate SQL schema
bob "Create SQL schema for an e-commerce database with users, products, orders, and order_items tables" --yolo --hide-intermediary-output > schema.sql

# Generate complex queries
bob "Create SQL queries for reporting: total sales by product, top customers, and monthly revenue" --yolo --hide-intermediary-output > reports.sql

# Generate with indexes
bob "Create SQL schema with appropriate indexes for a high-traffic blog application" --yolo --hide-intermediary-output > optimized-schema.sql
```

### ORMモデル

```bash
# Generate SQLAlchemy models
bob "Create SQLAlchemy models for a library management system with books, authors, and borrowers" --yolo --hide-intermediary-output > models.py

# Generate Sequelize models
bob "Create Sequelize models for an inventory system with products, categories, and suppliers" --yolo --hide-intermediary-output > models.js

# Generate Prisma schema
bob "Create a Prisma schema for a project management tool with projects, tasks, and users" --yolo --hide-intermediary-output > schema.prisma
```

### MongoDB操作

```bash
# Generate Mongoose schemas
bob "Create Mongoose schemas for a social network with users, posts, comments, and likes" --yolo --hide-intermediary-output > schemas.js

# Generate aggregation pipelines
bob "Create MongoDB aggregation pipelines for analytics: user engagement, popular posts, and activity trends" --yolo --hide-intermediary-output > aggregations.js
```

## テスト

### ユニットテスト

```bash
# Generate Jest tests
bob "Create Jest unit tests for a calculator class with add, subtract, multiply, and divide methods" --yolo --hide-intermediary-output > calculator.test.js

# Generate pytest tests
bob "Create pytest unit tests for a user authentication module with fixtures and mocks" --yolo --hide-intermediary-output > test_auth.py

# Generate with coverage
bob "Create comprehensive unit tests with edge cases for a string manipulation utility" --yolo --hide-intermediary-output > string-utils.test.js
```

### 統合テスト

```bash
# Generate API tests
bob "Create integration tests for a REST API using supertest with authentication and CRUD operations" --yolo --hide-intermediary-output > api.test.js

# Generate database tests
bob "Create integration tests for database operations with test database setup and teardown" --yolo --hide-intermediary-output > db.test.py
```

### E2Eテスト

```bash
# Generate Cypress tests
bob "Create Cypress E2E tests for a login flow with form validation and error handling" --yolo --hide-intermediary-output > login.cy.js

# Generate Playwright tests
bob "Create Playwright tests for a checkout process with multiple steps and payment" --yolo --hide-intermediary-output > checkout.spec.ts
```

## ユーティリティとヘルパー

### 文字列操作

```bash
# Generate string utilities
bob "Create utility functions for string manipulation: capitalize, slugify, truncate, and sanitize" --yolo --hide-intermediary-output > string-utils.js

# Generate with TypeScript
bob "Create TypeScript utility functions for string validation and formatting with type guards" --yolo --hide-intermediary-output > string-utils.ts
```

### 日付と時刻

```bash
# Generate date utilities
bob "Create utility functions for date manipulation: format, parse, add/subtract days, and timezone conversion" --yolo --hide-intermediary-output > date-utils.js

# Generate with moment.js
bob "Create date utility functions using moment.js for common date operations" --yolo --hide-intermediary-output > date-helpers.js
```

### 配列操作

```bash
# Generate array utilities
bob "Create utility functions for array operations: chunk, flatten, unique, groupBy, and sortBy" --yolo --hide-intermediary-output > array-utils.js

# Generate with lodash patterns
bob "Create custom array utility functions following lodash patterns with TypeScript" --yolo --hide-intermediary-output > array-utils.ts
```

### ファイル操作

```bash
# Generate file utilities
bob "Create Node.js utility functions for file operations: read, write, copy, delete with error handling" --yolo --hide-intermediary-output > file-utils.js

# Generate with async/await
bob "Create async file utility functions for batch processing and directory operations" --yolo --hide-intermediary-output > async-file-utils.js
```

## 高度なパターン

### デザインパターン

```bash
# Generate Singleton pattern
bob "Create a Singleton pattern implementation in JavaScript for a configuration manager" --yolo --hide-intermediary-output > singleton.js

# Generate Factory pattern
bob "Create a Factory pattern for creating different types of database connections" --yolo --hide-intermediary-output > db-factory.js

# Generate Observer pattern
bob "Create an Observer pattern implementation for an event system with TypeScript" --yolo --hide-intermediary-output > observer.ts

# Generate Strategy pattern
bob "Create a Strategy pattern for different payment methods with validation" --yolo --hide-intermediary-output > payment-strategy.js
```

### 非同期パターン

```bash
# Generate Promise utilities
bob "Create utility functions for Promise operations: retry, timeout, parallel, and sequential execution" --yolo --hide-intermediary-output > promise-utils.js

# Generate async queue
bob "Create an async queue implementation for rate-limited API calls" --yolo --hide-intermediary-output > async-queue.js

# Generate worker pool
bob "Create a worker pool for parallel processing of CPU-intensive tasks" --yolo --hide-intermediary-output > worker-pool.js
```

### エラーハンドリング

```bash
# Generate error classes
bob "Create custom error classes for different error types with stack traces and error codes" --yolo --hide-intermediary-output > errors.js

# Generate error handler middleware
bob "Create Express.js error handling middleware with logging and user-friendly messages" --yolo --hide-intermediary-output > error-handler.js

# Generate retry logic
bob "Create a retry mechanism with exponential backoff for failed operations" --yolo --hide-intermediary-output > retry.js
```

### キャッシング

```bash
# Generate cache implementation
bob "Create an in-memory cache with TTL, LRU eviction, and statistics" --yolo --hide-intermediary-output > cache.js

# Generate Redis cache wrapper
bob "Create a Redis cache wrapper with connection pooling and error handling" --yolo --hide-intermediary-output > redis-cache.js
```

### 認証

```bash
# Generate JWT utilities
bob "Create JWT utility functions for token generation, validation, and refresh with TypeScript" --yolo --hide-intermediary-output > jwt-utils.ts

# Generate OAuth implementation
bob "Create OAuth 2.0 implementation for Google authentication with Express.js" --yolo --hide-intermediary-output > oauth-google.js

# Generate password utilities
bob "Create password utility functions for hashing, validation, and strength checking using bcrypt" --yolo --hide-intermediary-output > password-utils.js
```

## 複数ファイル生成

### 完全なモジュール

```bash
# Generate complete feature module
bob "Create a complete user management module with routes, controllers, models, and tests. Provide the file structure and code for each component."

# Generate microservice
bob "Create a complete microservice for order processing with API, database, and message queue. Include all necessary files and configurations."

# Generate full-stack feature
bob "Create a full-stack todo feature with React frontend, Express backend, and MongoDB. Provide complete implementation for all layers."
```

### プロジェクトスキャフォールディング

```bash
# Generate project structure
bob "Create a complete Express.js project structure with best practices, middleware, and configuration. Include folder structure and key files."

# Generate React app structure
bob "Create a React application structure with routing, state management, and API integration. Provide the complete folder structure."

# Generate Python package
bob "Create a Python package structure with setup.py, tests, and documentation. Include all necessary configuration files."
```

## ベストプラクティス

### 1. 説明を具体的にする

```bash
# Good: Specific and detailed
bob "Create a React component for a user profile card with avatar image, full name, email, bio text, and edit button. Include loading state, error handling, and responsive design for mobile and desktop." --yolo --hide-intermediary-output > UserProfile.jsx

# Less effective: Too vague
bob "Create a user profile component" --yolo --hide-intermediary-output > UserProfile.jsx
```

### 2. 言語とフレームワークを指定する

```bash
# Explicit language specification
bob "Create a user authentication function in Python" --yolo --hide-intermediary-output > auth.py

# Explicit framework specification
bob "Create a form component in React with TypeScript" --yolo --hide-intermediary-output > Form.tsx
```

### 3. 要件を含める

```bash
# Include all requirements
bob "Create an Express.js API endpoint for user registration with:
- Email and password validation
- Password hashing with bcrypt
- JWT token generation
- Error handling for duplicate emails
- Input sanitization
- Rate limiting" --yolo --hide-intermediary-output > register.js
```

### 4. ドキュメントをリクエストする

```bash
# Request inline documentation
bob "Create a binary search function with detailed JSDoc comments explaining parameters, return value, and algorithm complexity" --yolo --hide-intermediary-output > binary-search.js

# Request examples
bob "Create a date formatting utility with usage examples in comments" --yolo --hide-intermediary-output > date-format.js
```

### 5. コードスタイルを指定する

```bash
# Request specific style
bob "Create a React component following Airbnb style guide with functional components and hooks" --yolo --hide-intermediary-output > Component.jsx

# Request modern patterns
bob "Create an async function using modern ES2022 features like top-level await and optional chaining" --yolo --hide-intermediary-output > modern.js
```

## トラブルシューティング

### 一般的な問題

1. **生成されたコードが期待と一致しない**
   - 説明をより具体的にする
   - 望ましい出力の例を含める
   - 正確なフレームワークバージョンを指定する

2. **依存関係が不足している**
   - package.jsonまたはrequirements.txtの生成をリクエストする
   - プロンプトで必要なすべてのライブラリを指定する

3. **コードスタイルの不一致**
   - スタイルガイド（Airbnb、Google、Standard）を指定する
   - リンティング設定をリクエストする

4. **不完全な実装**
   - 複雑なリクエストを小さな部分に分割する
   - 段階的に生成して組み合わせる

## より良い結果を得るためのヒント

1. **具体的にする**: プロンプトにすべての要件と制約を含める
2. **言語/フレームワークを言及**: 必要なテクノロジーを明示的に記述する
3. **テストをリクエスト**: 必要に応じてコードと一緒にテストを依頼する
4. **エッジケースを含める**: 処理すべきエッジケースを言及する
5. **型を依頼**: より良いコード品質のためにTypeScriptまたは型ヒントをリクエストする
6. **ドキュメントをリクエスト**: インラインコメントとドキュメントを依頼する
7. **エラーハンドリングを指定**: エラーハンドリングを明示的にリクエストする
8. **パフォーマンスを言及**: 必要に応じて最適化された実装を依頼する
9. **出力リダイレクトを使用**: `>`で生成されたコードを直接ファイルに保存する

## 例：完全な生成ワークフロー

```bash
# Generate a complete feature with all components
bob "Create a user authentication system in Node.js with Express including:
- User registration endpoint with email validation
- Login endpoint with JWT token generation
- Password hashing with bcrypt
- Middleware for protected routes
- Error handling
- Input validation
- Unit tests with Jest
Include detailed comments and follow best practices" --yolo --hide-intermediary-output > auth-system.js
```

## 次のステップ

- より多くのプロンプトパターンについては[基本コマンド](./basic-commands.md)をレビュー
- コードレビューについては[分析例](./analysis-examples.md)を探索
- 完全なワークフローについては[Lab 4 README](../README.md)を確認
- メインラボの演習で練習

---

**プロのヒント**: プロンプトが具体的で詳細であるほど、生成されるコードは良くなります。自然言語の説明に要件、制約、望ましいパターンを含めてください！