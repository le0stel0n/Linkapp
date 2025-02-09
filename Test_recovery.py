import unittest
from unittest.mock import MagicMock
from main_script import process_event

class TestEventProcessing(unittest.TestCase):
    """Unit tests for the event processing function."""

    def test_process_event(self):
        """Test that an event is processed correctly and recalculated."""
        event = {'id': 1, 'original_value': 100}
        
        # Call the process function
        result = process_event(event)
        
        # Check if recalculation is applied correctly
        self.assertEqual(result['recalculated_value'], 110.0)
        
        # Ensure status is updated
        self.assertEqual(result['status'], 'processed')

    def test_process_event_error_handling(self):
        """Test that processing handles errors gracefully."""
        event = {'id': 2}  # Missing 'original_value'

        # Call the process function, which should return None due to error
        result = process_event(event)
        
        # The result should be None as it fails due to missing data
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
