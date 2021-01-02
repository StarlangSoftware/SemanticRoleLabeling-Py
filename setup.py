from setuptools import setup

setup(
    name='NlpToolkit-SemanticRoleLabeling',
    version='1.0.0',
    packages=['SemanticRoleLabeling', 'SemanticRoleLabeling.Sentence', 'SemanticRoleLabeling.Sentence.FrameNet',
              'SemanticRoleLabeling.Sentence.Propbank', 'SemanticRoleLabeling.ParseTree',
              'SemanticRoleLabeling.ParseTree.Propbank'],
    url='https://github.com/StarlangSoftware/SemanticRoleLabeling-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Semantic Role Labeling Library',
    install_requires = ['NlpToolkit-AnnotatedSentence', 'NlpToolkit-AnnotatedTree']
)
