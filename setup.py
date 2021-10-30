from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='NlpToolkit-SemanticRoleLabeling',
    version='1.0.2',
    packages=['SemanticRoleLabeling', 'SemanticRoleLabeling.Sentence', 'SemanticRoleLabeling.Sentence.FrameNet',
              'SemanticRoleLabeling.Sentence.Propbank', 'SemanticRoleLabeling.ParseTree',
              'SemanticRoleLabeling.ParseTree.Propbank'],
    url='https://github.com/StarlangSoftware/SemanticRoleLabeling-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Semantic Role Labeling Library',
    install_requires = ['NlpToolkit-AnnotatedSentence', 'NlpToolkit-AnnotatedTree'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
