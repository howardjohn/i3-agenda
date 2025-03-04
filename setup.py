import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="i3-agenda",
    version="1.7",
    author="Tomer Rosenfeld",
    author_email="mail@tomerrosenfeld.com",
    description="Show your next google calendar event in polybar or i3-bar",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rosenpin/i3-agenda",
    download_url="https://github.com/rosenpin/i3-agenda/archive/1.7.tar.gz",
    packages=setuptools.find_packages(),
    license="Unlicense",
    classifiers=["Programming Language :: Python :: 3"],
    install_requires=[
        "python-bidi",
        "google-api-python-client",
        "google-auth-httplib2",
        "google-auth-oauthlib",
        "aiohttp",
    ],
    scripts=[
        "i3_agenda/config.py",
        "i3_agenda/event.py",
        "i3_agenda/API.py",
        "i3_agenda/cache_utils.py",
    ],
    entry_points={
        "console_scripts": [
            "i3-agenda = i3_agenda.i3_agenda:main",
        ],
    },
    python_requires=">=3.3",
)
