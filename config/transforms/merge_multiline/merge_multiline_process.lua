function(event, emit)
  local message = event.log.message or ""

  if type(message) ~= "string" or message == "" then
    return
  end

  -- print("Processing line: [" .. message .. "]")

  local is_start = false
  local start_patterns = {"^ERROR%s+", "^INFO%s+", "^WARN%s+", "^DEBUG%s+", "^TRACE%s+", "^FATAL%s+"}
  for i = 1, #start_patterns do
    if string.match(message, start_patterns[i]) then
      is_start = true
      break
    end
  end

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