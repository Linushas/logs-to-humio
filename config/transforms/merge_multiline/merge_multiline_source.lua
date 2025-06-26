state = {
  pending_event = nil
}

function timer_handler(emit)
  if state.pending_event then
    emit(state.pending_event)
  end

  state.pending_event = nil
  counter = 0
end