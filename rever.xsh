$PROJECT = 'toki'
$ACTIVITIES = [
    'version_bump',  # Changes the version number in various source files (setup.py, __init__.py, etc)
    'changelog',  # Uses files in the news folder to create a changelog for release
    'tag',  # Creates a tag for the new version number
    'push_tag',  # Pushes the tag up to the $TAG_REMOTE
    'pypi',  # Sends the package to pypi
    'conda_forge',  # Creates a PR into your package's feedstock
    'ghrelease'  # Creates a Github release entry for the new tag
]
# These note where/how to find the version numbers
$VERSION_BUMP_PATTERNS = [
    ('toki/__init__.py', '__version__\s*=.*', "__version__ = '$VERSION'"),
    ('setup.py', 'version\s*=.*,', "version='$VERSION',")
]
$CHANGELOG_FILENAME = 'docs/release-notes.md'  # Filename for the changelog
$CHANGELOG_TEMPLATE = 'TEMPLATE.md'  # Filename for the news template
$PUSH_TAG_REMOTE = 'git@github.com:toki-project/toki.git'  # Repo to push tags to

$GITHUB_ORG = 'toki-project'  # Github org for Github releases and conda-forge
$GITHUB_REPO = 'toki'  # Github repo for Github releases  and conda-forge
