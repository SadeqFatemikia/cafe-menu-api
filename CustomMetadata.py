from rest_framework.metadata import BaseMetadata


class CustomMetadata(BaseMetadata):
    def determine_metadata(self, request, view):
        return {
            'NAME': view.get_view_name(),
            'RENDERS': [renderer.media_type for renderer in view.renderer_classes],
            'PARSERS':[parser.media_type  for parser in view.parser_classes],
        }