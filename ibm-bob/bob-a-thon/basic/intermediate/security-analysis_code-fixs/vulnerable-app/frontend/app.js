/**
 * Todo Application - VULNERABLE VERSION
 * This code contains intentional XSS vulnerabilities for educational purposes.
 * DO NOT use this code in production!
 * 
 * Vulnerabilities:
 * - Using innerHTML with user content (XSS)
 * - No input sanitization
 * - Direct DOM manipulation with user data
 */

const API_URL = 'http://localhost:5000/api/todos';

let appState = {
    todos: [],
    isLoading: false,
    error: null
};

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    console.log('🚀 Todo App initialized (VULNERABLE VERSION)');
    setupEventListeners();
    fetchTodos();
});

function setupEventListeners() {
    const form = document.getElementById('todo-form');
    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const title = document.getElementById('todo-title').value.trim();
        const description = document.getElementById('todo-description').value.trim();
        
        if (!title) {
            alert('Please enter a todo title');
            return;
        }
        
        await createTodo(title, description);
    });
}

async function fetchTodos() {
    try {
        setLoadingState(true);
        const response = await fetch(API_URL);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const todos = await response.json();
        appState.todos = todos;
        appState.error = null;
        
        displayTodos(todos);
        console.log(`✅ Loaded ${todos.length} todos`);
        
    } catch (error) {
        console.error('❌ Error fetching todos:', error);
        appState.error = error.message;
        showErrorState('Failed to load todos. Please check if the backend is running.');
    } finally {
        setLoadingState(false);
    }
}

async function createTodo(title, description) {
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title: title,
                description: description
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const newTodo = await response.json();
        console.log('✅ Todo created:', newTodo);
        
        clearForm();
        await fetchTodos();
        
    } catch (error) {
        console.error('❌ Error creating todo:', error);
        alert('Failed to create todo. Please try again.');
    }
}

async function toggleTodo(todoId, completed) {
    try {
        const response = await fetch(`${API_URL}/${todoId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                completed: !completed
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        console.log(`✅ Todo ${todoId} toggled`);
        await fetchTodos();
        
    } catch (error) {
        console.error('❌ Error toggling todo:', error);
        alert('Failed to update todo. Please try again.');
    }
}

async function deleteTodo(todoId) {
    if (!confirm('Are you sure you want to delete this todo?')) {
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/${todoId}`, {
            method: 'DELETE'
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        console.log(`✅ Todo ${todoId} deleted`);
        await fetchTodos();
        
    } catch (error) {
        console.error('❌ Error deleting todo:', error);
        alert('Failed to delete todo. Please try again.');
    }
}

/**
 * VULNERABILITY: XSS through innerHTML
 * This function uses innerHTML to render user content, which allows
 * script injection if the user enters malicious HTML/JavaScript
 */
function displayTodos(todos) {
    const todosList = document.getElementById('todos-list');
    const emptyState = document.getElementById('empty-state');
    const todoCount = document.getElementById('todo-count');
    
    const count = todos.length;
    todoCount.textContent = `${count} ${count === 1 ? 'todo' : 'todos'}`;
    
    if (todos.length === 0) {
        todosList.innerHTML = '';
        emptyState.style.display = 'block';
        return;
    }
    
    emptyState.style.display = 'none';
    
    // VULNERABILITY: Using innerHTML with user content
    todosList.innerHTML = todos.map(todo => createTodoHTML(todo)).join('');
    
    // Attach event listeners
    todosList.querySelectorAll('.btn-success').forEach(button => {
        button.addEventListener('click', () => {
            const todoId = parseInt(button.dataset.id);
            const completed = button.dataset.completed === 'true';
            toggleTodo(todoId, completed);
        });
    });
    
    todosList.querySelectorAll('.btn-danger').forEach(button => {
        button.addEventListener('click', () => {
            const todoId = parseInt(button.dataset.id);
            deleteTodo(todoId);
        });
    });
}

/**
 * VULNERABILITY: Direct HTML injection
 * This function creates HTML with user input without any sanitization
 * Allows XSS attacks through todo.title and todo.description
 */
function createTodoHTML(todo) {
    const date = new Date(todo.created_at);
    const formattedDate = date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
    
    const completedClass = todo.completed ? 'completed' : '';
    const buttonText = todo.completed ? '↩️ Undo' : '✓ Complete';
    
    // VULNERABILITY: Direct insertion of user content into HTML
    // If todo.title contains <script>alert('XSS')</script>, it will execute!
    return `
        <div class="todo-item ${completedClass}">
            <div class="todo-header">
                <h3 class="todo-title">${todo.title}</h3>
            </div>
            ${todo.description ? `<p class="todo-description">${todo.description}</p>` : ''}
            <div class="todo-meta">
                <span class="todo-date">📅 ${formattedDate}</span>
                <div class="todo-actions">
                    <button 
                        class="btn btn-success" 
                        data-id="${todo.id}"
                        data-completed="${todo.completed}"
                    >
                        ${buttonText}
                    </button>
                    <button 
                        class="btn btn-danger" 
                        data-id="${todo.id}"
                    >
                        🗑️ Delete
                    </button>
                </div>
            </div>
        </div>
    `;
}

function setLoadingState(isLoading) {
    const loading = document.getElementById('loading');
    const todosList = document.getElementById('todos-list');
    
    appState.isLoading = isLoading;
    
    if (isLoading) {
        loading.style.display = 'block';
        todosList.style.display = 'none';
    } else {
        loading.style.display = 'none';
        todosList.style.display = 'block';
    }
}

function showErrorState(message) {
    const errorState = document.getElementById('error-state');
    const errorMessage = document.getElementById('error-message');
    const todosList = document.getElementById('todos-list');
    const emptyState = document.getElementById('empty-state');
    
    errorMessage.textContent = message;
    errorState.style.display = 'block';
    todosList.style.display = 'none';
    emptyState.style.display = 'none';
}

function clearForm() {
    document.getElementById('todo-title').value = '';
    document.getElementById('todo-description').value = '';
    document.getElementById('todo-title').focus();
}

console.log('⚠️ VULNERABLE VERSION - Contains XSS vulnerabilities!');

/**
 * HOW TO TEST THE XSS VULNERABILITY:
 * 
 * 1. Create a todo with this title:
 *    <img src=x onerror="alert('XSS Attack!')">
 * 
 * 2. Create a todo with this title:
 *    <script>alert('XSS')</script>
 * 
 * 3. Create a todo with this description:
 *    <img src=x onerror="document.body.innerHTML='<h1>Hacked!</h1>'">
 * 
 * These will execute JavaScript when the todo is displayed!
 */

// Made with Bob
