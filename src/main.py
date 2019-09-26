
from src.models.folder import Files


def main():

    files_instance = Files()
    new_folder_id = files_instance.create_folder('name_1')
    second_folder = files_instance.create_folder('name_2', new_folder_id)
    # file_instance = File('name_uno', '../media/photo.jpg', api_client.get_service())
    # new_file_id = file_instance.create(new_folder_id)

    print('First: ', new_folder_id)
    print('Second: ', second_folder)
    print("ALL WORK FINE")


if __name__ == '__main__':
    main()
