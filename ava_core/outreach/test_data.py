# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.outreach.models import Suspicious, ReportResponse, Question


class SuspiciousTestData(AvaCoreTestData):
    """
    Test data for Suspicious
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = Suspicious
    url = 'report/suspicious/'

    standard = {
        'suspicious_url': 'http://example.com',
        'question_ptr': 'default',
        'incident_date': '2016-01-31T09:00',
    }

    unique = {
        'suspicious_url': 'http://example1.com',
        'question_ptr': 'default',
        'incident_date': '2016-01-31T09:00',
    }


class ReportResponseTestData(AvaCoreTestData):
    """
    Test data for ReportResponse
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = ReportResponse
    url = 'report/response/'

    standard = {
        'message': 'standard_text',
        'question': 1,
        'owner': '',
    }

    unique = {
        'parent_response': 1,
        'message': 'unique_text',
        'question': 2,
        'owner': '',
    }


class QuestionTestData(AvaCoreTestData):
    """
    Test data for Question
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = Question
    url = 'report/question/'

    standard = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': 1,
        'status_type': 0,
        'suspicious': 'default',
        'question_responses': [],
        'priority_type': 0,
    }

    unique = {
        'is_resolved': False,
        'description': 'unique_text',
        'owner': 1,
        'status_type': 4,
        'suspicious': 'default',
        'question_responses': [],
        'priority_type': 3,
    }
