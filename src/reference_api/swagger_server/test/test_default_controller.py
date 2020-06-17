# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.approved_registries import ApprovedRegistries  # noqa: E501
from swagger_server.models.dataset_definition import DatasetDefinition  # noqa: E501
from swagger_server.models.dataset_list import DatasetList  # noqa: E501
from swagger_server.models.dataset_metadata import DatasetMetadata  # noqa: E501
from swagger_server.models.job_body import JobBody  # noqa: E501
from swagger_server.models.job_list import JobList  # noqa: E501
from swagger_server.models.job_results import JobResults  # noqa: E501
from swagger_server.models.job_status import JobStatus  # noqa: E501
from swagger_server.models.job_stop import JobStop  # noqa: E501
from swagger_server.models.selection_body import SelectionBody  # noqa: E501
from swagger_server.models.selection_success import SelectionSuccess  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_approved_registries_get(self):
        """Test case for approved_registries_get

        Get a List of Approved Container Registries
        """
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/approved_registries',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dataset_datasetid_definition_get(self):
        """Test case for dataset_datasetid_definition_get

        Get a Dataset Definition
        """
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/dataset/{datasetid}/definition'.format(datasetid='datasetid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dataset_datasetid_metadata_get(self):
        """Test case for dataset_datasetid_metadata_get

        Get Catalogue Entry (Metadata) for Dataset
        """
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/dataset/{datasetid}/metadata'.format(datasetid='datasetid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dataset_datasetid_selection_beacon_post(self):
        """Test case for dataset_datasetid_selection_beacon_post

        Get a Beacon (T/F) for a Specified Data Selection
        """
        body = SelectionBody()
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/selection/beacon',
            method='POST',
            data=json.dumps(body),
            content_type='application/text')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dataset_datasetid_selection_preview_post(self):
        """Test case for dataset_datasetid_selection_preview_post

        Preview the Results of a Selection Operation on a Dataset
        """
        body = SelectionBody()
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/selection/preview',
            method='POST',
            data=json.dumps(body),
            content_type='application/text')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dataset_datasetid_selection_profile_post(self):
        """Test case for dataset_datasetid_selection_profile_post

        Get a Profile of a Selection Operation on a Dataset
        """
        body = SelectionBody()
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/selection/profile',
            method='POST',
            data=json.dumps(body),
            content_type='application/text')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dataset_datasetid_selection_select_post(self):
        """Test case for dataset_datasetid_selection_select_post

        Perform a Selection Operation on a Dataset
        """
        body = SelectionBody()
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/selection/select',
            method='POST',
            data=json.dumps(body),
            content_type='application/text')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dataset_datasetid_selection_validate_post(self):
        """Test case for dataset_datasetid_selection_validate_post

        Validate a Given Selection
        """
        body = SelectionBody()
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/selection/validate',
            method='POST',
            data=json.dumps(body),
            content_type='application/text')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dataset_list_get(self):
        """Test case for dataset_list_get

        Get a List of Datasets that can be Filtered
        """
        query_string = [('doi', 'doi_example'),
                        ('title', 'title_example'),
                        ('author', 'author_example'),
                        ('description', 'description_example'),
                        ('organisation', 'organisation_example'),
                        ('tag_key', 'tag_key_example'),
                        ('tag_value', 'tag_value_example')]
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/dataset/list',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_health_check_get(self):
        """Test case for health_check_get

        Send Health Check Heartbeat
        """
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/health_check',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_job_jobid_results_get(self):
        """Test case for job_jobid_results_get

        Get the Results of a Job
        """
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/job/{jobid}/results'.format(jobid=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_job_jobid_status_get(self):
        """Test case for job_jobid_status_get

        Get the Status of a Job
        """
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/job/{jobid}/status'.format(jobid=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_job_jobid_stop_get(self):
        """Test case for job_jobid_stop_get

        Stop and Archive a Job
        """
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/job/{jobid}/stop'.format(jobid=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_job_list_get(self):
        """Test case for job_list_get

        Get a List of Submitted Jobs that can be Filtered
        """
        query_string = [('id', 'id_example'),
                        ('job_name', 'job_name_example'),
                        ('status', 'status_example')]
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/job/list',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_job_submit_post(self):
        """Test case for job_submit_post

        Submit a Compute Task
        """
        body = JobBody()
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/job/submit',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_job_validate_post(self):
        """Test case for job_validate_post

        Validate a Job Compute Task Specification
        """
        body = JobBody()
        response = self.client.open(
            '/gmcgilvary/Federated-Sharing-API-v1.1/1.1/job/validate'.format(id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
