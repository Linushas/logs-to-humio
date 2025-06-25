function(emit)
  if state.pending_event then
    emit(state.pending_event)
  end
end