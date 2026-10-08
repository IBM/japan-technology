"""
Data Processor - Analyzes CSV files and generates statistics

This Python script demonstrates various Python features that will be
translated to JavaScript in Lab 3:
- Type hints
- Context managers (with statement)
- List comprehensions
- Dictionary operations
- CSV and JSON handling
- Class-based design
"""

import csv
import json
from typing import List, Dict, Optional
from datetime import datetime
import os


class DataProcessor:
    """
    A class to process CSV data and generate statistical summaries.
    
    This class demonstrates common data processing patterns in Python
    that can be translated to other languages.
    """
    
    def __init__(self, filename: str) -> None:
        """
        Initialize the DataProcessor with a CSV filename.
        
        Args:
            filename: Path to the CSV file to process
        """
        self.filename = filename
        self.data: List[Dict[str, str]] = []
        self.stats: Dict[str, Dict[str, float]] = {}
    
    def load_data(self) -> None:
        """
        Load data from the CSV file.
        
        Uses Python's context manager (with statement) to safely
        handle file operations. The file is automatically closed
        even if an error occurs.
        
        Raises:
            FileNotFoundError: If the CSV file doesn't exist
            csv.Error: If the CSV file is malformed
        """
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"File not found: {self.filename}")
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                # List comprehension to read all rows
                self.data = [row for row in reader]
                
            print(f"✅ Loaded {len(self.data)} rows from {self.filename}")
            
        except csv.Error as e:
            raise csv.Error(f"Error reading CSV file: {e}")
    
    def calculate_statistics(self) -> Dict[str, Dict[str, float]]:
        """
        Calculate basic statistics for numeric fields in the data.
        
        This method demonstrates:
        - List comprehensions for filtering
        - Dictionary comprehensions
        - Built-in functions (sum, min, max, len)
        
        Returns:
            Dictionary with statistics for each numeric field:
            {
                'field_name': {
                    'mean': float,
                    'min': float,
                    'max': float,
                    'count': int
                }
            }
        """
        if not self.data:
            print("⚠️  No data loaded. Call load_data() first.")
            return {}
        
        # Find numeric fields using list comprehension
        # A field is considered numeric if its value can be converted to float
        numeric_fields = [
            key for key in self.data[0].keys()
            if self._is_numeric(self.data[0][key])
        ]
        
        print(f"📊 Found {len(numeric_fields)} numeric fields: {', '.join(numeric_fields)}")
        
        # Calculate statistics for each numeric field
        stats = {}
        for field in numeric_fields:
            # List comprehension to extract and convert values
            values = [float(row[field]) for row in self.data if self._is_numeric(row[field])]
            
            if values:
                stats[field] = {
                    'mean': sum(values) / len(values),
                    'min': min(values),
                    'max': max(values),
                    'count': len(values),
                    'sum': sum(values)
                }
        
        self.stats = stats
        return stats
    
    def _is_numeric(self, value: str) -> bool:
        """
        Check if a string value can be converted to a number.
        
        Args:
            value: String value to check
            
        Returns:
            True if the value is numeric, False otherwise
        """
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False
    
    def get_summary(self) -> Dict[str, any]:
        """
        Get a summary of the processed data.
        
        Returns:
            Dictionary containing data summary information
        """
        return {
            'filename': self.filename,
            'total_rows': len(self.data),
            'total_fields': len(self.data[0].keys()) if self.data else 0,
            'numeric_fields': len(self.stats),
            'processed_at': datetime.now().isoformat()
        }
    
    def export_results(self, output_file: str) -> None:
        """
        Export statistics to a JSON file.
        
        Args:
            output_file: Path to the output JSON file
            
        Raises:
            IOError: If unable to write to the output file
        """
        if not self.stats:
            print("⚠️  No statistics calculated. Call calculate_statistics() first.")
            return
        
        try:
            # Prepare output data
            output_data = {
                'summary': self.get_summary(),
                'statistics': self.stats
            }
            
            # Write to JSON file with pretty formatting
            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(output_data, file, indent=2)
            
            print(f"✅ Results exported to {output_file}")
            
        except IOError as e:
            raise IOError(f"Error writing to file: {e}")
    
    def print_statistics(self) -> None:
        """
        Print statistics to the console in a readable format.
        """
        if not self.stats:
            print("⚠️  No statistics available.")
            return
        
        print("\n" + "="*50)
        print("STATISTICS SUMMARY")
        print("="*50)
        
        for field, stats in self.stats.items():
            print(f"\n{field}:")
            print(f"  Mean:  {stats['mean']:.2f}")
            print(f"  Min:   {stats['min']:.2f}")
            print(f"  Max:   {stats['max']:.2f}")
            print(f"  Count: {stats['count']}")
            print(f"  Sum:   {stats['sum']:.2f}")
        
        print("\n" + "="*50)


def create_sample_data(filename: str = 'sample_data.csv') -> None:
    """
    Create a sample CSV file for testing.
    
    Args:
        filename: Name of the CSV file to create
    """
    sample_data = [
        {'name': 'Alice', 'age': '25', 'score': '95.5', 'grade': 'A'},
        {'name': 'Bob', 'age': '30', 'score': '87.3', 'grade': 'B'},
        {'name': 'Charlie', 'age': '22', 'score': '92.1', 'grade': 'A'},
        {'name': 'Diana', 'age': '28', 'score': '88.7', 'grade': 'B'},
        {'name': 'Eve', 'age': '26', 'score': '91.2', 'grade': 'A'},
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'age', 'score', 'grade'])
        writer.writeheader()
        writer.writerows(sample_data)
    
    print(f"✅ Created sample data file: {filename}")


def main():
    """
    Main function to demonstrate the DataProcessor usage.
    """
    print("🚀 Data Processor - Python Version")
    print("="*50)
    
    # Create sample data if it doesn't exist
    csv_file = 'sample_data.csv'
    if not os.path.exists(csv_file):
        create_sample_data(csv_file)
    
    try:
        # Initialize processor
        processor = DataProcessor(csv_file)
        
        # Load data
        processor.load_data()
        
        # Calculate statistics
        processor.calculate_statistics()
        
        # Print statistics to console
        processor.print_statistics()
        
        # Export to JSON
        processor.export_results('statistics.json')
        
        print("\n✅ Processing complete!")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


# Python idiom: only run main() if this file is executed directly
# (not when imported as a module)
if __name__ == '__main__':
    main()

# Made with Bob
