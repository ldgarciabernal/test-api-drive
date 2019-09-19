file_id = '1g6qh8K7rq5G2IbtGyTaHGjymIupaNnhY'
def callback(request_id, response, exception):
    if exception:
        # Handle error
        print exception
    else:
        print "Permission Id: %s" % response.get('id')

batch = drive_service.new_batch_http_request(callback=callback)
user_permission = {
    'type': 'user',
    'role': 'writer',
    'emailAddress': 'user@example.com'
}
batch.add(drive_service.permissions().create(
        fileId=file_id,
        body=user_permission,
        fields='id',
))
domain_permission = {
    'type': 'domain',
    'role': 'reader',
    'domain': 'example.com'
}
batch.add(drive_service.permissions().create(
        fileId=file_id,
        body=domain_permission,
        fields='id',
))
batch.execute()