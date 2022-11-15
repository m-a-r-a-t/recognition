import { combineReducers, configureStore } from '@reduxjs/toolkit';
import mainReducer from './reducers/MainSlice';

//Редьюсеры

const rootReducer = combineReducers({
  mainReducer
});

export const setupStore = () =>
  configureStore({
    reducer: rootReducer,
  });

export type RootState = ReturnType<typeof rootReducer>
export type AppStore = ReturnType<typeof setupStore>
export type AppDispatch = AppStore['dispatch']
