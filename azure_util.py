from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import os

class AzureUtility:
    def __init__(self, endpoint, key):
        self.endpoint = endpoint
        self.key = key
        self.document_analysis_client = DocumentAnalysisClient(
            endpoint=endpoint, credential=AzureKeyCredential(key)
        )

    # TODO: read_document() or read_excel() and read_pdf()?
    # TODO: Add error handling
    def read_document(self, form_url, model="prebuilt-invoice"):
        print("Reading document...")
        poller = self.document_analysis_client.begin_analyze_document_from_url(
            model, form_url
        )
        return poller.result()

    