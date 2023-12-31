from django.test import TestCase
from django_dynamic_fixture import get

from readthedocs.builds.constants import BUILD_STATE_BUILDING, BUILD_STATE_FINISHED
from readthedocs.builds.models import Build, Version
from readthedocs.projects.models import Project


class VersionConfigTests(TestCase):

    def setUp(self):
        self.project = get(Project)
        self.version = get(Version, project=self.project)

    def test_get_correct_config(self):
        build_old = Build.objects.create(
            project=self.project,
            version=self.version,
            _config={'version': 1},
            state=BUILD_STATE_FINISHED,
        )
        build_new = Build.objects.create(
            project=self.project,
            version=self.version,
            _config={'version': 2},
            state=BUILD_STATE_FINISHED,
        )
        build_new_error = Build.objects.create(
            project=self.project,
            version=self.version,
            _config={'version': 3},
            success=False,
            state=BUILD_STATE_FINISHED,
        )
        build_new_unfinish = Build.objects.create(
            project=self.project,
            version=self.version,
            _config={'version': 4},
            state=BUILD_STATE_BUILDING,
        )
        self.assertEqual(self.version.config, {'version': 2})

    def test_get_correct_config_when_same_config(self):
        build_old = get(
            Build,
            project=self.project,
            version=self.version,
            _config={},
            state=BUILD_STATE_FINISHED,
        )
        build_old.config = {'version': 1}
        build_old.save()

        build_new = get(
            Build,
            project=self.project,
            version=self.version,
            _config={},
            state=BUILD_STATE_FINISHED,
        )
        build_new.config = {'version': 1}
        build_new.save()

        build_new_error = get(
            Build,
            project=self.project,
            version=self.version,
            _config={},
            success=False,
            state=BUILD_STATE_FINISHED,
        )
        build_new_error.config = {'version': 3}
        build_new_error.save()

        build_new_unfinish = get(
            Build,
            project=self.project,
            version=self.version,
            _config={},
            state=BUILD_STATE_BUILDING,
        )
        build_new_unfinish.config = {'version': 1}
        build_new_unfinish.save()

        config = self.version.config
        self.assertEqual(config, {'version': 1})
