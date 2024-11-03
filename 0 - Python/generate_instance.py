import functions


def run():

    # Log the project directory
    functions.log_info('Project directory: ' + functions.get_project_directory())

    # Generate a new instance directory
    instance_directory = functions.generate_instance_directory('instances')

    # Add core instance files
    functions.add_core_files(instance_directory, '1 - Instance Core')

    # Add mods to instance
    unused_mods = functions.add_mods(instance_directory)

    # Add resource packs to instance
    functions.add_resource_packs(instance_directory)

    # Add shader packs to instance
    functions.add_shader_packs(instance_directory)

    # Log the unused mods
    if len(unused_mods) > 0:
        print()
        functions.log_warning('The following dependency mods included in the project are not required')
        print(unused_mods)
        print()


run()
