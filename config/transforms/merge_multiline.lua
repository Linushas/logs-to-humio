state = {
  pending_event = nil
}
start_pattern = "^(TRACE|FATAL|INFO|ERROR|WARN|DEBUG)%s"
hooks:
  process: |
    function(event, emit)
      local message = event.log.message or ""

      if type(message) ~= "string" or message == "" then
        return
      end

      local is_start = string.match(message, start_pattern)

      if is_start then
        if state.pending_event then
          emit(state.pending_event)
        end

        state.pending_event = event
      else
        if state.pending_event then
          state.pending_event.log.message = state.pending_event.log.message .. "\n" .. message
        end
      end

      return
    end
  shutdown: |
    function(emit)
      if state.pending_event then
        emit(state.pending_event)
      end
    end