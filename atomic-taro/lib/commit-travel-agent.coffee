{Point, Range, TextBuffer} = require 'atom'


module.exports =
class CommitTravelAgent

  constructor: (@masterVariant, @atomicTaroView) ->
    @mainMenuHeader = @masterVariant.getHeaderElement()
    @outputPane = null


  '''
    added later after the output pane initializes
  '''
  setOutputPane: (out) ->
    @outputPane = out


  travelToGlobalCommit: (commit) ->
    # check if we are in the current state or in the past
    # make sure the editor is not editable
    # travel text of master variant and set all nested variants back

    # update all commit lines to show which commit we're on
    # update all branch maps to show which branch each variant is on
    # show a lock icon that makes it clear that you cannot editor
    # have the option to show this past whatever into an editable branch
    # compare/diff

    # update the main menu to show the new commit
    @mainMenuHeader.showAlertPane(commit)

    @masterVariant.getModel().travelToCommit(commit)
    # style all variants so it's clear we're in the past
    @masterVariant.travelStyle()


  '''
    Any variant can call this method. This is at the global program level so that
    we can coordinate multiple components, such as the output pane and diffs.
  '''
  resetToPresent: (variant) ->
    variant.getModel().backToTheFuture()
    variant.removeTravelStyle()
    @outputPane.backToTheFuture()



  localTravel: (commit) ->
    # if travel only in a local variant, don't change the whole filePath
    # but make the output from that commit available and
    # also somehow give the user the ability to go back to the entire
    # file that created (those)that output at this commit
