def to_braket(array):
    """ helper for pretty printing """
    state = []
    basis = ('|00>', '|10>', '|01>', '|11>')
    for im, base_state in zip(array, basis):
        if im:
            if abs(im.imag)>0.001:
                state.append(f'{im.real:.1f}{base_state}')
            else:
                state.append(f'({im:.1f}){base_state}')

    return " + ".join(state)
