	import azure.cosmos.cosmos_client as cosmos_client
	import azure.cosmos.exceptions as exceptions
	from azure.cosmos.partition_key import PartitionKey
	
	HOST = 'https://<CosmosServerName>.documents.azure.com:443/'
	MASTER_KEY = '<PrimaryKey>'
	DATABASE_ID = '<DatabaseName>'
	CONTAINER_ID = '<ContainerName>'
	
	def query_items(container):
	    items = list(container.query_items(
	        query="SELECT r.id, r.name, r.age, r.gender FROM root r",
	        enable_cross_partition_query=True
	    ))
	
	    print(items)
	
	def run_sample():
	    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart", user_agent_overwrite=True)
	
	    try:
	        try:
	            db = client.get_database_client(database=DATABASE_ID)
	        except exceptions.CosmosResourceExistsError:
	            pass
	
	        try:
	            container = db.get_container_client(CONTAINER_ID)
	        except exceptions.CosmosResourceExistsError:
	            pass
	
	        query_items(container)
	
	    except exceptions.CosmosHttpResponseError as e:
	        print('\nrun_sample has caught an error. {0}'.format(e.message))
	
	if __name__ == '__main__':
	    run_sample()
