#first run:
#  plugin install river-couchdb
curl -XDELETE 'http://localhost:9200/brock/'
curl -XDELETE 'http://localhost:9200/_river/'
curl -XPUT 'localhost:9200/_river/brock/_meta' -d '{
    "type" : "couchdb",
    "couchdb" : {
        "host" : "localhost",
        "port" : 5984,
        "db" : "brock",
        "filter" : null
    },
    "index" : {
        "index" : "brock",
        "type" : "brock",
        "bulk_size" : "100",
        "bulk_timeout" : "10ms"
    }
}'
#        "store": {
#          "type": "memory"
#        }
curl -XGET 'localhost:9200/_status'
curl -XPOST 'http://localhost:9200/_refresh'
#in config/default-mapping.json
#{ 
#    "_default" : { 
#        "properties" : { 
#            "created" : {"type" : "string"},
#            "cdmcreated" : {"type" : "string"},
#            "cdmmodified" : {"type" : "string"},
#            "available" : {"type" : "string"},
#            "temporal" : {"type" : "string"}
#        } 
#    } 
#}' 
