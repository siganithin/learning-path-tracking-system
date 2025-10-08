import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Add src to path

class Subject:
    def __init__(self, subject_id, name):
        self.subject_id = subject_id
        self.name = name
