# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import Any, AsyncIterable, Awaitable, Callable, Iterable, Sequence, Tuple, Optional

from google.cloud.billing_v1.types import cloud_billing


class ListBillingAccountsPager:
    """A pager for iterating through ``list_billing_accounts`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.billing_v1.types.ListBillingAccountsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``billing_accounts`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBillingAccounts`` requests and continue to iterate
    through the ``billing_accounts`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.billing_v1.types.ListBillingAccountsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., cloud_billing.ListBillingAccountsResponse],
            request: cloud_billing.ListBillingAccountsRequest,
            response: cloud_billing.ListBillingAccountsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.billing_v1.types.ListBillingAccountsRequest):
                The initial request object.
            response (google.cloud.billing_v1.types.ListBillingAccountsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_billing.ListBillingAccountsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[cloud_billing.ListBillingAccountsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[cloud_billing.BillingAccount]:
        for page in self.pages:
            yield from page.billing_accounts

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListBillingAccountsAsyncPager:
    """A pager for iterating through ``list_billing_accounts`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.billing_v1.types.ListBillingAccountsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``billing_accounts`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBillingAccounts`` requests and continue to iterate
    through the ``billing_accounts`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.billing_v1.types.ListBillingAccountsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[cloud_billing.ListBillingAccountsResponse]],
            request: cloud_billing.ListBillingAccountsRequest,
            response: cloud_billing.ListBillingAccountsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.billing_v1.types.ListBillingAccountsRequest):
                The initial request object.
            response (google.cloud.billing_v1.types.ListBillingAccountsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_billing.ListBillingAccountsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[cloud_billing.ListBillingAccountsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[cloud_billing.BillingAccount]:
        async def async_generator():
            async for page in self.pages:
                for response in page.billing_accounts:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListProjectBillingInfoPager:
    """A pager for iterating through ``list_project_billing_info`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.billing_v1.types.ListProjectBillingInfoResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``project_billing_info`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListProjectBillingInfo`` requests and continue to iterate
    through the ``project_billing_info`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.billing_v1.types.ListProjectBillingInfoResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., cloud_billing.ListProjectBillingInfoResponse],
            request: cloud_billing.ListProjectBillingInfoRequest,
            response: cloud_billing.ListProjectBillingInfoResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.billing_v1.types.ListProjectBillingInfoRequest):
                The initial request object.
            response (google.cloud.billing_v1.types.ListProjectBillingInfoResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_billing.ListProjectBillingInfoRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[cloud_billing.ListProjectBillingInfoResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[cloud_billing.ProjectBillingInfo]:
        for page in self.pages:
            yield from page.project_billing_info

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListProjectBillingInfoAsyncPager:
    """A pager for iterating through ``list_project_billing_info`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.billing_v1.types.ListProjectBillingInfoResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``project_billing_info`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListProjectBillingInfo`` requests and continue to iterate
    through the ``project_billing_info`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.billing_v1.types.ListProjectBillingInfoResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[cloud_billing.ListProjectBillingInfoResponse]],
            request: cloud_billing.ListProjectBillingInfoRequest,
            response: cloud_billing.ListProjectBillingInfoResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.billing_v1.types.ListProjectBillingInfoRequest):
                The initial request object.
            response (google.cloud.billing_v1.types.ListProjectBillingInfoResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_billing.ListProjectBillingInfoRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[cloud_billing.ListProjectBillingInfoResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[cloud_billing.ProjectBillingInfo]:
        async def async_generator():
            async for page in self.pages:
                for response in page.project_billing_info:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
