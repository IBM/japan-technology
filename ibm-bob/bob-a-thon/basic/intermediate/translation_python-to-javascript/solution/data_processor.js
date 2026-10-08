/**
 * Data Processor - Analyzes CSV files and generates statistics
 * Translated from Python to JavaScript (Node.js)
 * 
 * This JavaScript implementation demonstrates how Python features
 * are translated to JavaScript equivalents:
 * - Type hints → JSDoc comments
 * - Context managers → Promises and async/await
 * - List comprehensions → Array methods (map, filter)
 * - Dictionary operations → Object operations
 * - CSV and JSON handling → Node.js modules
 */

const fs = require('fs').promises;
const { createReadStream } = require('fs');
const csv = require('csv-parser');
const path = require('path');


/**
 * A class to process CSV data and generate statistical summaries.
 * 
 * This class demonstrates common data processing patterns translated
 * from Python to JavaScript.
 */
class DataProcessor {
    /**
     * Initialize the DataProcessor with a CSV filename.
     * 
     * @param {string} filename - Path to the CSV file to process
     */
    constructor(filename) {
        this.filename = filename;
        this.data = [];
        this.stats = {};
    }
    
    /**
     * Load data from the CSV file.
     * 
     * Uses Node.js streams and csv-parser to read CSV files.
     * This is the JavaScript equivalent of Python's context manager
     * with csv.DictReader.
     * 
     * @returns {Promise<void>}
     * @throws {Error} If the CSV file doesn't exist or is malformed
     */
    async loadData() {
        try {
            // Check if file exists
            await fs.access(this.filename);
            
            // Read CSV file using streams (async operation)
            return new Promise((resolve, reject) => {
                const results = [];
                
                createReadStream(this.filename)
                    .pipe(csv())
                    .on('data', (row) => {
                        results.push(row);
                    })
                    .on('end', () => {
                        this.data = results;
                        console.log(`✅ Loaded ${this.data.length} rows from ${this.filename}`);
                        resolve();
                    })
                    .on('error', (error) => {
                        reject(new Error(`Error reading CSV file: ${error.message}`));
                    });
            });
            
        } catch (error) {
            throw new Error(`File not found: ${this.filename}`);
        }
    }
    
    /**
     * Calculate basic statistics for numeric fields in the data.
     * 
     * This method demonstrates JavaScript equivalents of Python features:
     * - List comprehensions → Array.filter() and Array.map()
     * - Built-in functions → Math methods and Array.reduce()
     * 
     * @returns {Object} Dictionary with statistics for each numeric field
     */
    calculateStatistics() {
        if (this.data.length === 0) {
            console.log('⚠️  No data loaded. Call loadData() first.');
            return {};
        }
        
        // Find numeric fields
        // JavaScript equivalent of Python list comprehension
        const numericFields = Object.keys(this.data[0])
            .filter(key => this._isNumeric(this.data[0][key]));
        
        console.log(`📊 Found ${numericFields.length} numeric fields: ${numericFields.join(', ')}`);
        
        // Calculate statistics for each numeric field
        const stats = {};
        for (const field of numericFields) {
            // Extract and convert values (equivalent to Python list comprehension)
            const values = this.data
                .filter(row => this._isNumeric(row[field]))
                .map(row => parseFloat(row[field]));
            
            if (values.length > 0) {
                stats[field] = {
                    mean: values.reduce((a, b) => a + b, 0) / values.length,
                    min: Math.min(...values),
                    max: Math.max(...values),
                    count: values.length,
                    sum: values.reduce((a, b) => a + b, 0)
                };
            }
        }
        
        this.stats = stats;
        return stats;
    }
    
    /**
     * Check if a string value can be converted to a number.
     * 
     * @param {string} value - String value to check
     * @returns {boolean} True if the value is numeric, False otherwise
     * @private
     */
    _isNumeric(value) {
        // JavaScript equivalent of Python's try/except for type conversion
        const num = parseFloat(value);
        return !isNaN(num) && isFinite(num);
    }
    
    /**
     * Get a summary of the processed data.
     * 
     * @returns {Object} Dictionary containing data summary information
     */
    getSummary() {
        return {
            filename: this.filename,
            total_rows: this.data.length,
            total_fields: this.data.length > 0 ? Object.keys(this.data[0]).length : 0,
            numeric_fields: Object.keys(this.stats).length,
            processed_at: new Date().toISOString()
        };
    }
    
    /**
     * Export statistics to a JSON file.
     * 
     * Uses Node.js fs.promises for async file writing,
     * equivalent to Python's context manager with json.dump.
     * 
     * @param {string} outputFile - Path to the output JSON file
     * @returns {Promise<void>}
     * @throws {Error} If unable to write to the output file
     */
    async exportResults(outputFile) {
        if (Object.keys(this.stats).length === 0) {
            console.log('⚠️  No statistics calculated. Call calculateStatistics() first.');
            return;
        }
        
        try {
            // Prepare output data
            const outputData = {
                summary: this.getSummary(),
                statistics: this.stats
            };
            
            // Write to JSON file with pretty formatting
            // JSON.stringify with indent=2 is equivalent to Python's json.dump with indent=2
            await fs.writeFile(
                outputFile,
                JSON.stringify(outputData, null, 2),
                'utf8'
            );
            
            console.log(`✅ Results exported to ${outputFile}`);
            
        } catch (error) {
            throw new Error(`Error writing to file: ${error.message}`);
        }
    }
    
    /**
     * Print statistics to the console in a readable format.
     */
    printStatistics() {
        if (Object.keys(this.stats).length === 0) {
            console.log('⚠️  No statistics available.');
            return;
        }
        
        console.log('\n' + '='.repeat(50));
        console.log('STATISTICS SUMMARY');
        console.log('='.repeat(50));
        
        for (const [field, stats] of Object.entries(this.stats)) {
            console.log(`\n${field}:`);
            console.log(`  Mean:  ${stats.mean.toFixed(2)}`);
            console.log(`  Min:   ${stats.min.toFixed(2)}`);
            console.log(`  Max:   ${stats.max.toFixed(2)}`);
            console.log(`  Count: ${stats.count}`);
            console.log(`  Sum:   ${stats.sum.toFixed(2)}`);
        }
        
        console.log('\n' + '='.repeat(50));
    }
}


/**
 * Create a sample CSV file for testing.
 * 
 * @param {string} filename - Name of the CSV file to create
 * @returns {Promise<void>}
 */
async function createSampleData(filename = 'sample_data.csv') {
    const sampleData = [
        { name: 'Alice', age: '25', score: '95.5', grade: 'A' },
        { name: 'Bob', age: '30', score: '87.3', grade: 'B' },
        { name: 'Charlie', age: '22', score: '92.1', grade: 'A' },
        { name: 'Diana', age: '28', score: '88.7', grade: 'B' },
        { name: 'Eve', age: '26', score: '91.2', grade: 'A' }
    ];
    
    // Convert to CSV format
    const headers = Object.keys(sampleData[0]);
    const csvContent = [
        headers.join(','),
        ...sampleData.map(row => headers.map(h => row[h]).join(','))
    ].join('\n');
    
    await fs.writeFile(filename, csvContent, 'utf8');
    console.log(`✅ Created sample data file: ${filename}`);
}


/**
 * Main function to demonstrate the DataProcessor usage.
 * 
 * This is the JavaScript equivalent of Python's if __name__ == '__main__'
 */
async function main() {
    console.log('🚀 Data Processor - JavaScript Version');
    console.log('='.repeat(50));
    
    // Create sample data if it doesn't exist
    const csvFile = 'sample_data.csv';
    try {
        await fs.access(csvFile);
    } catch {
        await createSampleData(csvFile);
    }
    
    try {
        // Initialize processor
        const processor = new DataProcessor(csvFile);
        
        // Load data (async operation)
        await processor.loadData();
        
        // Calculate statistics
        processor.calculateStatistics();
        
        // Print statistics to console
        processor.printStatistics();
        
        // Export to JSON (async operation)
        await processor.exportResults('statistics.json');
        
        console.log('\n✅ Processing complete!');
        
    } catch (error) {
        if (error.message.includes('File not found')) {
            console.error(`❌ Error: ${error.message}`);
        } else {
            console.error(`❌ Unexpected error: ${error.message}`);
        }
        process.exit(1);
    }
}


// JavaScript equivalent of Python's if __name__ == '__main__':
// Only run main() if this file is executed directly (not imported)
if (require.main === module) {
    main().catch(error => {
        console.error('❌ Fatal error:', error.message);
        process.exit(1);
    });
}


// Export the class for use as a module
module.exports = DataProcessor;


/**
 * TRANSLATION NOTES:
 * 
 * Python → JavaScript Mappings:
 * 
 * 1. Type Hints → JSDoc Comments
 *    Python: def load_data(self) -> None:
 *    JavaScript: @returns {Promise<void>}
 * 
 * 2. Context Managers → Async/Await
 *    Python: with open(file) as f:
 *    JavaScript: await fs.promises.readFile()
 * 
 * 3. List Comprehensions → Array Methods
 *    Python: [x for x in list if condition]
 *    JavaScript: list.filter(x => condition)
 * 
 * 4. Dictionary Comprehensions → Object Building
 *    Python: {k: v for k, v in dict.items()}
 *    JavaScript: Object.entries(dict).reduce()
 * 
 * 5. Built-in Functions → Math/Array Methods
 *    Python: sum(values) / len(values)
 *    JavaScript: values.reduce((a,b) => a+b) / values.length
 * 
 * 6. Exception Handling → Try/Catch
 *    Python: try/except
 *    JavaScript: try/catch
 * 
 * 7. String Formatting → Template Literals
 *    Python: f"text {variable}"
 *    JavaScript: `text ${variable}`
 * 
 * 8. Module Execution Check
 *    Python: if __name__ == '__main__':
 *    JavaScript: if (require.main === module)
 */

// Made with Bob
