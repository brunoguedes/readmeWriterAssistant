import os
from dotenv import load_dotenv

import streamlit as st

from readmewriterassistant.files_manager import FilesManager
from readmewriterassistant.llms import LLMs

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class App:
    def generate_readme_for_project_structure(self, llm, project_structure, files_content):
        prompt = PromptTemplate(
            input_variables = ['project_structure', 'files_content'], 
            template = """
Act as a python developer, specialized in writing projects documentations.

Given a project with the structure bellow:

```
{project_structure}
```

and with the content of each files bellow:
{files_content}

Write a Readme.md file, using markdown format, for this project.

"""
        )

        readme_for_project_structure_chain = LLMChain(llm=llm, prompt=prompt, verbose=True, output_key='job_requirements_summary')
        return readme_for_project_structure_chain.run(project_structure=project_structure, files_content=files_content)

    def run(self):
        st.title('README.md Writer Assistant')

        # LLM Picker
        llms = LLMs()
        chosen_llm = st.selectbox(
            "Please select the model you'd like to use:",
            llms.get_available_llms(),
            index=0,
        )
        llm = llms.get_llm(chosen_llm)

        # Input Fields
        exclude_list = st.text_input("Enter the names of the folders or files you'd like to exclude (comma-separated)", value="tests, README.md, .gitignore, poetry.lock, ")
        exclude_list = [item.strip() for item in exclude_list.split(',')]
        base_path = st.text_input('Enter the folder you want to generate the ReadMe.md from', value='./')

        st.subheader('Folder Structure:')
        fm = FilesManager()
        files = fm.list_files(base_path=base_path, exclude=exclude_list)
        project_structure = fm.format_file_tree(file_list=files)
        st.code(project_structure)
        st.divider()
        
        
        if st.button('Generate ReadMe.md'):
            files_content = fm.read_files_content(base_path=base_path, items=files)
            readme_for_project_structure = self.generate_readme_for_project_structure(llm=llm, project_structure=project_structure, files_content=files_content)
            st.header('README.md')
            st.code(readme_for_project_structure)

if __name__ == "__main__":
    load_dotenv()
    app = App()
    app.run()