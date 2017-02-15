Images are stored in collections, known as a repository, which is keyed by a name, as seen throughout the API specification. A registry instance may contain several repositories. The list of available repositories is made available through the catalog.

The catalog for a given registry can be retrieved with the following request:

`GET /v2/_catalog`