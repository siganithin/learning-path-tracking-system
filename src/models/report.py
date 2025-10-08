import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Add src to path

class Report:
    def __init__(self, report_id, plan_id, summary):
        self.report_id = report_id
        self.plan_id = plan_id
        self.summary = summary
