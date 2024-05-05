import os
from dotenv import load_dotenv

import streamlit as st

from readmewriterassistant.files_manager import FilesManager
from readmewriterassistant.llms import LLMs

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class App:
    def generate_readme_for_project_structure(self, llm, project_structure):
        prompt = PromptTemplate(
            input_variables = ['project_structure'], 
            template = """
Act as a python developer, specialized in writing projects documentation used by other developers. Your goal is to create readme files using markdown format.

Readme files should contain:
- A summary of the project and a list of features.
- A high level overview of the code, including the project structure.
- Installation instructions.
- A list of dependencies.
- Instructions on how to configure and use/run.
- Acknowledgements of third party code.
- Contribution guidelines.
- License information.

Given a project with the structure bellow:

```
{project_structure}
```

Create a initial Readme.md file, for this project, including the project structure as given.

"""
        )
        chain = LLMChain(llm=llm, prompt=prompt, verbose=True, output_key='readme_output')
        return chain.run(project_structure=project_structure)

    def update_readme_for_file(self, llm, readme, file_content):
        prompt = PromptTemplate(
            input_variables = ['readme', 'file_content'], 
            template = """
                Act as a python developer, specialized in writing projects documentation used by other developers. Your goal is to update the readme, keeping the markdown.
                
                Readme files should contain:
                - A summary of the project and a list of features.
                - A high level overview of the code, including the project structure.
                - Installation instructions.
                - A list of dependencies.
                - Instructions on how to configure and use/run.
                - Acknowledgements of third party code.
                - Contribution guidelines.
                - License information.

                Given the readme bellow:

                ```
                {readme}
                ```

                Update the readme, adding/updating any relevant information obtained from the content of the file bellow:

                ```
                {file_content}
                ```
                """
        )

        chain = LLMChain(llm=llm, prompt=prompt, verbose=True, output_key='readme_output')
        return chain.run(readme=readme, file_content=file_content)

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
        # llm_max_context_length = llms.get_max_context_length(chosen_llm)

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
            readme_for_project_structure = self.generate_readme_for_project_structure(llm=llm, project_structure=project_structure)
            updated_readme = readme_for_project_structure
            st.header('README.md')
            for item in files:
                file_content = fm.read_file_content(base_path=base_path, file=item)
                updated_readme = self.update_readme_for_file(llm=llm, readme=updated_readme, file_content=file_content)
            st.code(updated_readme)

if __name__ == "__main__":
    load_dotenv()
    app = App()
    app.run()