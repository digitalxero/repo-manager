# Repo Manager
General purpose package repository manager that supports plugable metadata generators, and storage backends

###	Command Line API
* **manage-repo**
 *  **create** *repo_name*
   * Create a new empty repo *repo_name* for all known metadata generators
  * **add** *repo_name* *package*
    * Add a new package to the specified repo. Generate metadata for all applicable meta data generators based on file extentions, and metadata provided with the package
  * **remove** *repo_name* *package*
    * Remove a package from the specified repo. Remove metadata from all applicable meta data generators based on file extentions, and metadata provided with the package
  * **delete** *repo_name*
    * delete all packages and metadata associated with <repo_name>
  * **rebuild** *repo_name*
    * delete all metadata associated with <repo_name> and rescan all packages to rebuild the metadata

###	Application Architecture
* MetaData Generators (eg apt, yum, pacman, pkg(BSD version), etc)
  * Each MetaData Generator must know how to analyze a package to determine if the package applies and beable to generate all MetaData required for that repo type
  * Packages should be able to provide hints in meta data to assist in this analysis

* Package Storage Backends
  * plugable API to create arbitrary package storage backends
  * eg LocalStorage, SwiftStorage, S3Storage, etc

* MetaData Storage Backends
  * plugable API to create arbitrary metadata storage backends
  * eg LocalStorage, RedisStorage, DBStorage, etc

### Web API
* /repos/
  * **GET** List all repos

* /repos/:repo_name/
  * **POST** Create repository :repo_name
  * **GET** List all packages in :repo_name
  * **DELETE** delete repo :repo_name
  * **TRACE** rebuild repo :repo_name

* /repos/:repo_name/packages/
  * **GET** List all packages in :repo_name
  * **POST** (file contents posted) add package to :repo_name

* /repos/:repo_name/packages/:package_name/
  * **GET** download :package_name from :repo_name (may be a 301/305/307 response to redirect to the storage backend url)
  * **DELETE** remove :package_name from :repo_name

* /repos/:repo_name/repodata/*
  * **GET** return the yum repo metadata for :repo_name

* /repos/:repo_name/dist/*
  * **GET** return the apt metadata for :repo_name

#### Notes
The reason we need two sperate storage backends is because the metadata must be updated atomically, where as saving a package to storage does not need to be atomic so for the metadata we need a backend that allows locking or CAS (Check & Set)
