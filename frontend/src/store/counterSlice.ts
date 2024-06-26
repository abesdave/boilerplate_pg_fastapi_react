import type { PayloadAction } from "@reduxjs/toolkit"
import { createAppSlice } from "./createAppSlice"
import { AppThunk } from "./store"

export interface CounterSliceState {
    value: number
    status: "idle" | "loading" | "failed"
}

const initialState: CounterSliceState = {
    value: 0,
    status: "idle",
}

export const counterSlice = createAppSlice({
    name: "counter",
    initialState,
    reducers: create => ({
        increment: create.reducer(state => {
            state.value += 1
        }),
        decrement: create.reducer(state => {
            state.value -= 1
        }),
        incrementByAmount: create.reducer(
            (state, action: PayloadAction<number>) => {
                state.value += action.payload
            },
        ),
        incrementAsync: create.asyncThunk(
            async (amount: number) => {
                const response = await new Promise<{ data: number }>(resolve =>
                    setTimeout(() => resolve({ data: amount }), 500),
                )

                return response.data
            },
            {
                pending: state => {
                    state.status = "loading"
                },
                fulfilled: (state, action) => {
                    state.status = "idle"
                    state.value += action.payload
                },
                rejected: state => {
                    state.status = "failed"
                },
            },
        ),
    }),
    selectors: {
        selectCount: counter => counter.value,
        selectStatus: counter => counter.status,
    },
})

export const { decrement, increment, incrementByAmount, incrementAsync } = counterSlice.actions
export const { selectCount, selectStatus } = counterSlice.selectors

// We can also write thunks by hand, which may contain both sync and async logic.
// Here's an example of conditionally dispatching actions based on current state.
export const incrementIfOdd =
  (amount: number): AppThunk =>
  async (dispatch, getState) => {
    const currentValue = await selectCount(getState())

    if (currentValue % 2 === 1 || currentValue % 2 === -1) {
      dispatch(incrementByAmount(amount))
    }
  }
