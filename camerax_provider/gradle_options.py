from pythonforandroid.recipe import Recipe

class GradleOptionsRecipe(Recipe):
    name = 'gradle_options'
    depends = []
    conflicts = []

    def should_build(self):
        return False

    def get_gradle_dependencies(self):
        return ['androidx.camera:camera-core:1.3.0',
                'androidx.camera:camera-camera2:1.3.0',
                'androidx.camera:camera-lifecycle:1.3.0']

recipe = GradleOptionsRecipe()
