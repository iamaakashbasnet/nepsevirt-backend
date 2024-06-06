import axios from 'axios';
import { toast } from 'react-toastify';

import { store } from 'state/store';
import { loadUserDataAsync } from 'state/user/authSlice';

export interface StockNames {
  id: number;
  name: string;
}

export interface StockDetail extends StockNames {
  ltp: number;
  open: number;
  high: number;
  low: number;
  close: number;
}

export interface StockBuyResponse {
  stock: number;
}

export const fetchStockNames = async () => {
  try {
    const res = await axios.get<StockNames[]>('/api/data/live-data-stockname/');
    return res.data;
  } catch (err) {
    if (axios.isAxiosError(err) && err.response) {
      toast.error(err.response.data as string);
    }
  }
};

export const fetchStockDetail = async (id: number) => {
  try {
    const res = await axios.get<StockDetail>(`/api/data/stock-detail/${id}/`);
    return res.data;
  } catch (err) {
    if (axios.isAxiosError(err) && err.response) {
      toast.error(err.response.data as string);
    }
  }
};

export const buyStock = async (quantity: number, stock: number) => {
  try {
    const res = await axios.post<StockBuyResponse>(`/api/trade/buy/`, { quantity: Number(quantity), stock: stock });
    toast.success('Order executed successfully.');
    await store.dispatch(loadUserDataAsync());
    return res.data;
  } catch (err) {
    if (axios.isAxiosError(err) && err.response) {
      toast.error(err.response.data as string);
    }
  }
};

export const sellStock = async (quantity: number, stock: number) => {
  try {
    const res = await axios.post<StockBuyResponse>(`/api/trade/sell/`, { quantity: Number(quantity), stock: stock });
    toast.success('Order executed successfully.');
    await store.dispatch(loadUserDataAsync());
    return res.data;
  } catch (err) {
    if (axios.isAxiosError(err) && err.response) {
      toast.error(err.response.data as string);
    }
  }
};
