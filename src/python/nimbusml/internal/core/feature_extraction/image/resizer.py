# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Resizer
"""

__all__ = ["Resizer"]


from ....entrypoints.transforms_imageresizer import transforms_imageresizer
from ....utils.utils import trace
from ...base_pipeline_item import BasePipelineItem, DefaultSignature


class Resizer(BasePipelineItem, DefaultSignature):
    """

    Resizers an image to a specified dimension using a specified
    resizing method.

    .. remarks::
        ``Resizer`` resizers an image to the specified height and width
        using a specified resizing method. The input variables to this
        transforms must
        be images, typically the result of the ``Loader`` transform.

    :param image_width: Specifies the width of the scaled image in pixels.
        The default value is 224.

    :param image_height: Specifies the height of the scaled image in pixels.
        The default value is 224.

    :param resizing: Specified the resizing method to use. Note that all
        methods
        are using bilinear interpolation. The options are:

        * ``"IsoPad"``: The image is resizerd such that the aspect ratio is
        preserved.
          If needed, the image is padded with black to fit the new width or
        height.
        * ``"IsoCrop"``: The image is resizerd such that the aspect ratio is
        preserved.
          If needed, the image is cropped to fit the new width or height.
        * ``"Aniso"``: The image is stretched to the new width and height,
        without
          preserving the aspect ratio.

        The default value is ``"IsoCrop"``.

    :param crop_anchor: Anchor for cropping.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`Loader <nimbusml.feature_extraction.image.Loader>`,
        :py:class:`PixelExtractor
        <nimbusml.feature_extraction.image.PixelExtractor>`.

    .. index:: transform, image

    Example:
       .. literalinclude:: /../nimbusml/examples/Image.py
              :language: python
    """

    @trace
    def __init__(
            self,
            image_width=0,
            image_height=0,
            resizing='IsoCrop',
            crop_anchor='Center',
            **params):
        BasePipelineItem.__init__(
            self, type='transform', **params)

        self.image_width = image_width
        self.image_height = image_height
        self.resizing = resizing
        self.crop_anchor = crop_anchor

    @property
    def _entrypoint(self):
        return transforms_imageresizer

    @trace
    def _get_node(self, **all_args):

        input_columns = self.input
        if input_columns is None and 'input' in all_args:
            input_columns = all_args['input']
        if 'input' in all_args:
            all_args.pop('input')

        output_columns = self.output
        if output_columns is None and 'output' in all_args:
            output_columns = all_args['output']
        if 'output' in all_args:
            all_args.pop('output')

        # validate input
        if input_columns is None:
            raise ValueError(
                "'None' input passed when it cannot be none.")

        if not isinstance(input_columns, list):
            raise ValueError(
                "input has to be a list of strings, instead got %s" %
                type(input_columns))

        # validate output
        if output_columns is None:
            output_columns = input_columns

        if not isinstance(output_columns, list):
            raise ValueError(
                "output has to be a list of strings, instead got %s" %
                type(output_columns))

        algo_args = dict(
            column=[
                dict(
                    Source=i,
                    Name=o) for i,
                o in zip(
                    input_columns,
                    output_columns)] if input_columns else None,
            image_width=self.image_width,
            image_height=self.image_height,
            resizing=self.resizing,
            crop_anchor=self.crop_anchor)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)