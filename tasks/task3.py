import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
import os
import tempfile
import uuid

class DocumentProcessor:
    def __init__(self):
        self.pages=[]

    def ingest_documents(self):
        uploaded_files=st.file_uploader('Upload Files',type=['pdf'],accept_multiple_files=True)
        if uploaded_files is not None:
            for uploaded_file in uploaded_files:
                unique_id=uuid.uuid4().hex
                original_name,file_extension=os.path.splitext(uploaded_file.name)
                temp_file_name=f"{original_name}_{unique_id}{file_extension}"
                temp_file_path=os.path.join(tempfile.gettempdir(),temp_file_name)
            
                with open(temp_file_path,'wb') as f:
                    f.write(uploaded_file.getvalue())
                loader=PyPDFLoader(temp_file_path)
                pages_x=loader.load_and_split()
                for p in pages_x:
                    self.pages.append(p)
                os.unlink(temp_file_path)
            st.write(f"Total Pages processed:{len(self.pages)}")
if __name__=="__main__":
    processor=DocumentProcessor()
    processor.ingest_documents()


